<font size='4'><b>opentodo</b></font><br />
_Система управления задачами на Django_

  * <a href='http://code.google.com/p/opentodo/#Что_такое_opentodo?'>Что такое opentodo?</a><br />
  * <a href='http://code.google.com/p/opentodo/#Демо'>Демо</a><br />
  * <a href='http://code.google.com/p/opentodo/#Скриншоты'>Скриншоты</a><br />
  * <a href='http://code.google.com/p/opentodo/#Установка_и_настройка'>Установка и настройка</a><br />
  * <a href='http://code.google.com/p/opentodo/#Автор'>Автор</a><br />

# Что такое opentodo? #

Это инструмент для организации совместной работы над проектами, система управления задачами с веб-интерфейсом.<br />**opentodo** написана на языке Python ([Django Framework](http://www.djangoproject.com/)).


## Особенности ##

  * Простой, удобный интерфейс в стиле Gmail

  * Добавление задач, назначение ответственных и сроков выполнения

  * Возможность прикреплять файлы к задачам и проектам - скриншоты, документацию и т.п.

  * Жизненный цикл задач: Новая, Принята, Завершена, Одобрена

  * Цветовое кодирование задач в зависимости от статуса

  * Комментарии к задачам

  * E-mail уведомления

  * Управление пользователями с помощью стандартной панели администрирования Django

  * Разграничение доступа пользователей к проектам <b>(новое в версии 0.9)</b>

<br />
# Демо #

http://demo.opentodo.ru/ - вход в демо-версию opentodo

<br />
# Скриншоты #

[![](http://opentodo.ru/screenshots/task_list_small.gif)](http://opentodo.ru/screenshots/)

<br />
# Установка и настройка #

Все достаточно просто и стандартно, как и для любого другого приложения на Django.
Но для полной ясности приведу инструкцию, которую рекомендуется прочитать перед началом работы. Предполагается, что Django уже установлен, и вы знаете как настроить веб-сервер для обслуживания Django-проектов.

<ol>
<li>Скачайте архив с последней версией opentodo.<br>
<br>
Или скопируйте код из системы контроля версий:<br>
<pre><code>git clone git://github.com/mgrigoriev/opentodo.git<br>
</code></pre>

</li><li>Скопируйте директорию <code>opentodo</code> из архива туда, где располагаются ваши проекты Django.<br />Будем считать, что теперь проект находится здесь - <code>/var/django_projects/opentodo</code> и по окончании настройки будет доступен по адресу <code>http://myhost.ru/</code>

</li><li>Скопируйте содержимое директории <code>opentodo_media</code> из архива в какое-нибудь место за пределами проекта Django, которое веб-сервер обслуживает напрямую.<br>
Директория <code>opentodo_media</code> должна физически располагаться на том же сервере, что и проект.<br>
Допустим, что вы скопировали сюда: <code>/var/www/opentodo_media</code>

В <code>opentodo_media</code> находится вся статика (css, javascript, изображения), а также подкаталог <code>upload</code>, в который будут загружаться файлы - проверьте наличие прав на запись.<br>
<br>
Будем считать, что веб-сервер обслуживает директорию <code>opentodo_media</code> по адресу <code>http://static.myhost.ru</code>

</li><li>Создайте базу данных. Пусть это будет база данных MySQL, которая называется <code>opentodo</code>, логин и пароль: <code>user123/mypasswd</code><br />При создании базы данных выберите кодировку UTF-8.<br>
<br>
</li><li>Теперь отредактируем настройки.<br />
Создайте файл <code>local_settings.py</code>, скопировав шаблон <code>local_settings.py.default</code>:<br>
<br>
<pre><code>cp local_settings.py.default local_settings.py<br>
</code></pre>

Отредактируйте файл <code>local_settings.py</code>:<br>
<br>
<pre><code>DATABASE_NAME = 'opentodo'<br>
DATABASE_USER = 'user123'<br>
DATABASE_PASSWORD = 'mypasswd'<br>
<br>
MEDIA_ROOT = '/var/www/opentodo_media'<br>
MEDIA_URL = 'http://static.myhost.ru'   # Если содержит путь после url, не забудьте слэш в конце, например:<br>
                                        # http://myhost.ru/static/<br>
</code></pre>

Это все основные настройки.<br>
Можно дополнительно настроить почтовые уведомления, отредактировав параметры авторизации на почтовом сервере - <code>EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD</code>.<br>
<br>
В завершении, исправьте несколько случайных символов в значении <code>SECRET_KEY</code>, чтобы оно было уникальным.<br>
<br>
</li><li>Теперь осталось создать таблицы в базе данных:<br>
<pre><code>cd /var/django_projects/opentodo<br>
python manage.py syncdb<br>
</code></pre>

Когда будут создаваться таблицы системы управления пользователями, вам будет предложено создать аккаунт администратора - введите логин, e-mail и пароль.<br>
<br>
</li><li>Вот и все, осталось перезапустить веб-сервер.<br>
Откройте в браузере страницу <code>http://myhost.ru/</code>, и должна появиться форма авторизации.<br>
Введите логин и пароль, который вы указали на этапе создания таблиц базы данных (пункт 6).<br>
<br>
</li><li>Для добавления новых пользователей в систему воспользуйтесь стандартной панелью управления Django (<code>http://myhost.ru/admin/</code>)</li>
</ol>

<br />
# Автор #

**Михаил Григорьев**<br />

**E-mail:** [mgrigoriev@gmail.com](mailto:mgrigoriev@gmail.com)<br />
**Мой Круг**: http://m-grigorev.moikrug.ru