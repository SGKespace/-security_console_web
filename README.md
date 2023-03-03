# main.py
Пульт охраны банка. 
Пульт охраны - это сайт, который берет данные из удаленных баз (визиты и пропуска сотруднков).
После запуска 'пульт' доступен по адресу: http://127.0.0.1:8000. 

# Требования к окружению
```
Python 3.xx и выше (должен быть уже установлен)
django==3.2.*
psycopg2-binary==2.9.*
django-debug-toolbar==3.2
environs==9.5.0
```
Можно установить командой  
``` 
PIP install -r requirements.txt
```
# Переменные окружения
Пример файла .env
```
DB_ENGINE='django.db.backends.postgresql_psycopg2'
DB_HOST='checkpoint.devman.org'
DB_PORT='5434'
DB_NAME='checkpoint'
DB_USER='guard'
DB_PASSWORD='osim5'

SECRET_KEY='REPLACE_ME'

DEBUG=TRUE

ALLOWED_HOSTS=['*']
```
Для того чтобы запустить скрипт, войдите в директорию со скриптом и запустите команду:
```
 python3 manage.py runserver
```
# Примеры успешного запуска скрипта:

<img width="1073" alt="image" src="https://user-images.githubusercontent.com/55636018/221362213-aaa41155-b01e-4b68-a27f-0108f3ae796e.png">

<img width="1072" alt="image" src="https://user-images.githubusercontent.com/55636018/221362241-c271bddc-2875-4f05-9de7-b95283326bd3.png">

<img width="1050" alt="image" src="https://user-images.githubusercontent.com/55636018/221362290-88c00e9c-4b24-4a96-b2fa-d8632e4db0f2.png">


## Отказ от ответственности

Автор программы не несет никакой ответственности за то, как вы используете этот код или как вы используете сгенерированные с его помощью данные. Эта программа была написана для обучения автора и других целей не несет. Не используйте данные, сгенерированные с помощью этого кода в незаконных целях.
