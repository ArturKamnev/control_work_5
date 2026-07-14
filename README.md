
### 1. Клонировать репозиторий

```bash
git clone https://github.com/ArturKamnev/control_work_5.git
cd control_work_5
```

### 2. Создать виртуальное окружение

```bash
python -m venv venv
```

Активация на Windows:

```bash
venv\Scripts\activate
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Создать базу данных PostgreSQL

Создайте базу данных, например:

```text
blog_db
```

### 5. Настроить переменные окружения

Создайте файл `.env` в корне проекта и заполните его:

```env
NAME_DB=blog_db
USER_DB=postgres
PASSWORD_DB=your_password
HOST_DB=127.0.0.1
PORT_DB=5432

SECRET_KEY=your_secret_key
DEBUG=on
```

Замените `your_password` на пароль пользователя PostgreSQL.

### 6. Применить миграции

```bash
python manage.py migrate
```

### 7. Запустить сервер

```bash
python manage.py runserver
```

После запуска API будет доступно по адресу:

```text
http://127.0.0.1:8000/
```

## Документация API

Swagger:

```text
http://127.0.0.1:8000/swagger/
```

ReDoc:

```text
http://127.0.0.1:8000/redoc/
```

## Авторизация

### Регистрация

```text
POST /api/v1/users/register/
```

Пример тела запроса:

```json
{
  "username": "artur",
  "password": "password123",
  "password_confirm": "password123"
}
```

### Получение токена

```text
POST /api/v1/users/login/
```

Пример тела запроса:

```json
{
  "username": "artur",
  "password": "password123"
}
```

Полученный токен нужно передавать в заголовке:

```text
Authorization: Token your_token
```