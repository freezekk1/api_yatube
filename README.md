# API Yatube

`API Yatube` - REST API для социальной платформы с публикациями, комментариями, группами и подписками.
Сервис позволяет читать контент без авторизации, а для создания и изменения данных использует JWT-токены.

## Что умеет проект

- работать с постами и комментариями;
- отдавать список групп и детали группы;
- создавать подписки на авторов и искать по ним;
- выдавать и обновлять JWT-токены.

## Технологии

- Python 3.10
- Django 3.2
- Django REST Framework
- Simple JWT

## Как запустить проект локально

1. Клонировать репозиторий:

```bash
git clone <repo_url>
cd api-final-yatube-ad
```

2. Создать и активировать виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate
```

Для Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

3. Установить зависимости:

```bash
pip install -r requirements.txt
```

4. Выполнить миграции и запустить сервер:

```bash
cd yatube_api
python manage.py migrate
python manage.py runserver
```

Документация будет доступна по адресу `http://127.0.0.1:8000/redoc/`.

## Примеры запросов

Получение JWT-токена:

```http
POST /api/v1/jwt/create/
Content-Type: application/json

{
  "username": "TestUser",
  "password": "1234567"
}
```

Создание поста:

```http
POST /api/v1/posts/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "text": "Новый пост",
  "group": 1
}
```

Создание подписки:

```http
POST /api/v1/follow/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "following": "TestUserAnother"
}
```

Получение комментариев поста:

```http
GET /api/v1/posts/1/comments/
```
