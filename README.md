# API для Yatube

`api-final-yatube-ad-vlad` — учебный backend-проект на Django REST Framework для социальной платформы Yatube. Он предоставляет API для публикаций, комментариев, сообществ и подписок, а также JWT-аутентификацию для защищённых операций.

## Что умеет API

- выдаёт список постов и отдельные публикации;
- создаёт, редактирует и удаляет посты автора;
- возвращает список сообществ и информацию о группе;
- позволяет получать, создавать, редактировать и удалять комментарии к постам;
- поддерживает подписки на авторов и поиск по подпискам;
- выдаёт JWT-токены для авторизации.

Неавторизованные пользователи могут только читать данные. Изменение контента и работа с `/follow/` доступны только авторизованным пользователям.

## Технологии

- Python 3.11
- Django 3.2
- Django REST Framework 3.12
- Simple JWT
- SQLite

## Как запустить проект локально

1. Клонируйте репозиторий:

```bash
git clone https://github.com/911-boy/api-final-yatube-ad-vlad.git
cd api-final-yatube-ad-vlad
```

2. Создайте и активируйте виртуальное окружение.

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Выполните миграции:

```bash
cd yatube_api
python manage.py migrate
```

5. Запустите сервер:

```bash
python manage.py runserver
```

После запуска документация будет доступна по адресу:

`http://127.0.0.1:8000/redoc/`

## Примеры запросов

Получить JWT-токен:

```http
POST /api/v1/jwt/create/
Content-Type: application/json

{
  "username": "TestUser",
  "password": "1234567"
}
```

Создать пост:

```http
POST /api/v1/posts/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "text": "Новый пост",
  "group": 1
}
```

Получить комментарии к посту:

```http
GET /api/v1/posts/1/comments/
```

Подписаться на автора:

```http
POST /api/v1/follow/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "following": "TestUserAnother"
}
```

## Основные эндпоинты

- `GET /api/v1/posts/`
- `GET /api/v1/posts/{id}/`
- `POST /api/v1/posts/`
- `PUT/PATCH/DELETE /api/v1/posts/{id}/`
- `GET /api/v1/groups/`
- `GET /api/v1/groups/{id}/`
- `GET /api/v1/posts/{post_id}/comments/`
- `POST /api/v1/posts/{post_id}/comments/`
- `GET/PUT/PATCH/DELETE /api/v1/posts/{post_id}/comments/{id}/`
- `GET /api/v1/follow/`
- `POST /api/v1/follow/`
- `POST /api/v1/jwt/create/`
- `POST /api/v1/jwt/refresh/`
- `POST /api/v1/jwt/verify/`
