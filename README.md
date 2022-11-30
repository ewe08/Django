# Django
## Инструкция по запуску:
### 1. В папке lyceum создать файл .env с аргументами "ключ=значение". </br>
Пример _.env_:
```
SECRET_KEY=django-...
DEBUG_MODE=True
ALLOWED_HOSTS=127.0.0.1 localhost
```
### 2. Выполнить команды через консоль:
Ставим виртуальное окружение:

> python3 -m venv venv </br>

Активируем окружение:
> . venv/bin/activate (или venv/Scripts/activate для Windows) </br>

Качаем библиотеки:
> pip install -r requirements.txt </br>

### 3. Запуск сервера
Выполняем:
```
cd lyceum
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Для просмотра по умолчанию переходим на: http://127.0.0.1:8000/ или http://localhost:8000/
## База данных

![image](https://user-images.githubusercontent.com/56339316/204703954-f48cc8a5-c999-4720-9b03-3a83c6ebce4a.png)
