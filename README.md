# Техническое задание на реализацию блога

## Технический стек

- ЯП - Python `3.10`
- Стек технологий для реализации бэкенд: `FastAPI` + `SQLAlchemy`  
- База данных - `PostgreSQL`
- Развертывание проекта с помощью `Docker` (Docker-Compose)

## Задание

### Реализовать блог со следующими возможностями:

#### Управление постами

- создание, изменение и удаление постов
    - создание поста
        - входные данные
            - автор поста
            - тема поста
            - содержимое поста
        - выходные данные
            - успешность выполнения
    - изменение поста
        - входные данные
            - идентификатор поста
            - автор поста
            - тема поста
            - содержимое поста
        - выходные данные
            - успешность выполнения
    - удаление поста
        - входные данные
            - идентификатор поста
        - выходные данные
            - успешность выполнения

#### Отображение постов

> Фронтенд (работа с браузером) реализовывается средствами бэкенда (например, с использованием Jinja)

- отображение постов на странице веб-браузера

#### Управление комментариями и добавление в избранное

- отображение лайков, поставленных конкретному посту
- модификация количества лайков
    - увеличение количества лайков
        - входные данные
            - идентификатор поста
        - выходные данные
            - успешность выполнения
    - уменьшение количества лайков
        - входные данные
            - идентификатор поста
        - выходные данные
            - успешность выполнения

### Данные в БД должны содержать

- идентификатор поста
- тему поста
- содержимое поста
- количество лайков
- автора поста
- дату публикации

### Блог должен быть развернут в Docker — т.е. должна быть конфигурация для выполнения данной операции

### Приветствуется:

- реализация дополнительного функционала за пределами указанного ТЗ
- использование сериализаторов/десериализаторов
- использование миграций

---

# Запуск приложения

## План действий

1. Клонируйте репозиторий: `git clone ...`
2. Перейдите в папку проекта
3. Создайте файлы `.db-env` и `.post_manager-env` с вашими значениями
4. Запустите команду докера: `docker-compose ud -d --build`
5. Откройте в браузере ссылку http://localhost:8501. Откроется web приложение для взаимодействия
6. Так же есть swagger http://localhost:8080/docs

### Содержимое `.db-env`

```dotenv
POSTGRES_USER=имя-пользователя
POSTGRES_PASSWORD=пароль
POSTGRES_DB=название-БД
PGDATA=/var/lib/postgresql/data/pgdata
```

### Содержимое `.post_manager-env`

```dotenv
POSTGRES_USER=имя-пользователя
POSTGRES_PASSWORD=пароль
POSTGRES_HOST=название-контейнера-с-БД
POSTGRES_DB=название-БД
```

---

# Некоторые команды для работы с миграциями

### :desktop_computer: Настройте структуру базы через миграции

```commandline
alembic upgrade head
```

### Просмотреть историю миграций:

```commandline
alembic history
```

### Посмотреть на какой мы сейчас миграции находимся:

```commandline
alembic current
```

### Создать новую миграцию:

```commandline
alembic revision --autogenerate -m "Оставляйте осмысленное описание изменений"  
```

### Откатиться на одну миграцию:

```commandline
alembic downgrade -1
```

### При удалении миграции необходимо:

1. Откатить миграцию `alembic downgrade -1`
2. Удалить файл миграции

Если не делать откат, то будет конфликт миграций alembic

---

### Настройка линтера

Все настройки линтера находятся в файле .flake8

### TODO

#### post_manager

- offset для crud операций на стороне backend'a
- кеширование запросов
- аутентификация и авторизация пользователей

#### newsline

- страница регистрации/аутентификации 
- получение автора из сессии после аутентификации/авторизации
- страница автора
  - редактирование
  - удаление
  - профиль
- страница постов
  - обновление данных поста
  - удаление поста
  - комментирование постов
