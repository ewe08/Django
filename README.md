# Django
### Инструкция по запуску:
Для клонирования (Скачаивания проекта) себе на компьютер:

- **Для Windows**
    1. Убедитесь, что на компьютере установлен git и python
    2. Заходим в коммандную строку (терминал) 
    3. Пишем: </br> ```git clone https://github.com/ewe08/Django.git``` </br>
    (Может не работать из-за двухфакторной аутентификация) 
    4. ```cd Django\lyceum``` 
    5. ```python -m venv venv``` 
    6. ```venv\Scripts\activate```
    7. ```pip install -r requirements.txt```
    8. Создаём файл .env и вписываем туда:
        ```
        DEBUG=True 
        SECRET_KEY = '...' (Секретный ключ) 
        ALLOWED_HOSTS='["*"]' 
        INTERNAL_IPS='["127.0.0.1", "localost"]' 
        DEFAULT_FROM_EMAIL = 'djangoLearning@support.com'
        ```
    9. Выполняем миграции:<br> 
    ```python manage.py makemigrations```</br>
    ```python manage.py migrate```
    
    10. Создадим админа: </br> ```python manage.py createsuperuser```   
    11. ```python3 manage.py runserver```
    12. Поздавляю! Проект работает! 
</br> 

- **Для Linux/MacOS**
    1. Убедитесь, что на компьютере установлен git и python
    2. Заходим в коммандную строку (терминал) 
    3. Пишем: </br> ```git clone https://github.com/ewe08/Django.git``` </br>
    (Может не работать из-за двухфакторной аутентификация) 
    4. ```cd Django\lyceum``` 
    5. ```python3 -m venv venv``` 
    6. ```source venv\bin\activate```
    7. ```pip3 install -r requirements.txt```
    8. Создаём файл .env и вписываем туда:
        ```
        DEBUG=True 
        SECRET_KEY = '...' (Секретный ключ) 
        ALLOWED_HOSTS='["*"]' 
        INTERNAL_IPS='["127.0.0.1", "localost"]' 
        DEFAULT_FROM_EMAIL = 'djangoLearning@support.com'
        ```
    9. Выполняем миграции:<br> 
    ```python3 manage.py makemigrations```</br>
    ```python3 manage.py migrate```
    10. Создадим админа: </br> ```python3 manage.py createsuperuser```   
    11. ```python3 manage.py runserver```
    12. Поздавляю! Проект работает! 
</br>

### Если нам нужны тестовые данные:
- **Для Windows**
    * ```copy bd_example.sqlite3 db.sqlite3```

- **Для Linux/MacOS**
    * ```cp bd_example.sqlite3 db.sqlite3```

### Для запуска проекта в dev режиме:
- **Для Windows**
    1. Убедитесь, что в проете есть настроенный .env
    2. Убедитесь, что в терминале активированно виртуальное окружение 
    3. ```python manage.py runserver```

- **Для Linux/MacOS**
    1. Убедитесь, что в проете есть настроенный .env
    2. Убедитесь, что в терминале активированно виртуальное окружение 
    3. ```python3 manage.py runserver```
## База данных
![image](https://user-images.githubusercontent.com/56339316/205954000-bc97df3d-e392-410b-93bd-12cbf8e0387a.png)
