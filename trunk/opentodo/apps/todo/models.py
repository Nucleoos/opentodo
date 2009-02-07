# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

# Генерирует upload path для FileField
def make_upload_path(instance, filename):
    upload_path = "uploads"
    if isinstance(instance, ProjectAttach):
        project_id = instance.project.id
        return u"%s/%s/%s" % (upload_path, project_id, filename)

    elif isinstance(instance, TaskAttach):
        project_id = instance.task.project.id
        return u"%s/%s/tasks/%s" % (upload_path, project_id, filename)    

# Проекты (группы задач)
class Project(models.Model):
    title = models.CharField("Проект", max_length=255)
    info = models.TextField("Описание", null=True, blank=True)
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)
    author = models.ForeignKey(User, null=True, db_column='author', related_name="projects", verbose_name="Автор")
    def __unicode__(self):
        return self.title
    def _get_tasks_count(self):
        return self.related_tasks.count()
    def _get_tasks_count_active(self):
        return self.related_tasks.exclude(status=3).exclude(status=4).count()
    tasks_count = property(_get_tasks_count)
    tasks_active_count = property(_get_tasks_count_active)

# Статусы задач
class Status(models.Model):
    title = models.CharField("Статус", max_length=50)
    def __unicode__(self):
        return self.title

# Задачи
class Task(models.Model):
    project = models.ForeignKey(Project, verbose_name="Проект", related_name="related_tasks")
    status = models.ForeignKey(Status, default=1, verbose_name="Статус")
    author = models.ForeignKey(User, null=True, db_column='author', related_name="tasks", verbose_name="Автор")
    assigned_to = models.ForeignKey(User, null=True, db_column='assigned_to', related_name="assigned_tasks", verbose_name="Ответственный")
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)
    title =  models.CharField("Задача", max_length=255)
    info = models.TextField("Описание", null=True, blank=True)
    deadline = models.DateField("Срок", null=True, blank=True)
    has_deadline = models.BooleanField(default=0)
    def __unicode__(self):
        return self.title

# Комментарии к задачам
class Comment(models.Model):
    task = models.ForeignKey(Task, related_name="comments")
    author = models.ForeignKey(User)
    message = models.TextField("Комментарий")
    created_at = models.DateTimeField("Дата", auto_now_add=True)
    class Meta:
        ordering = ['created_at']

# Абстрактный класс для файлов-вложений
class CommonAttach(models.Model):
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    attached_file = models.FileField(upload_to=make_upload_path)
    class Meta:
        abstract=True

# Аттачи к проектам
class ProjectAttach(CommonAttach):
    project = models.ForeignKey(Project, related_name="files")

# Аттачи к задачам
class TaskAttach(CommonAttach):
    task = models.ForeignKey(Task, related_name="files")