# REST API для Yatube.
- `Yatube` - это социальная сеть, где можно публиковать свои мысли,
описывать значимые для себя события и выражать эмоции текстом. Так же
можно объединяться в группы по интересам и подписываться на полюбившегося автора.
- `REST API для Yatube` - это интерфейс через, который смогут работать мобильные приложения или чат-бот.
Либо передавать данные в веб-приложение или на фронтенд.
## Инструменты:
- `Django REST Framework` - фреймворк вклюяающий в чебя набор инструментов для создания REST-сервисов на основе Django.
- `Djoser` - приложения для настройки токенов авторизации.

## Как запустить проект:
### Клонировать репозиторий и перейти в него в командной строке:

`git clone https://github.com/Pankirbor/api_final_yatube.git`

`cd api_final_yatube`

### Cоздать и активировать виртуальное окружение:

`python3 -m venv env`

`source env/bin/activate`

`python3 -m pip install --upgrade pip`

### Установить зависимости из файла requirements.txt:

`pip install -r requirements.txt`

### Выполнить миграции:

`cd yatube_api`

`python3 manage.py migrate`

### Запустить проект:

`python3 manage.py runserver`

### Примеры запросов к API
- Для получения JWT-токена:

`POST /api/v1/jwt/create/`

```python
{
    "username": "string",
    "password": "string"
}
```
- Для получения конкретного поста:

`GET /api/v1/posts/{id}/`

Ответ:

```python
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
- Для размещения поста:

`POST /api/v1/posts/`

```python
{
    "text": "string",
    "image": "string",
    "group": 0
}
```
Ответ:

```python
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
- Для получения списка сообществ:

`GET /api/v1/groups/`

Ответ:

```python
[
    {
        "id": 0,
        "title": "string",
        "slug": "string",
        "description": "string"
    },
    ...
]
```
- Для получения списка комментариев к посту:

`GET /api/v1/posts/{post_id}/comments/`

Ответ:

```python
[
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "created": "2019-08-24T14:15:22Z",
        "post": 0
    },
    ...
]
```
### Разработчик
- Кирилл Панов при поддержке команды ЯндексПрактикум.