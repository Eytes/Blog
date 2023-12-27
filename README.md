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

# Инструкции для тестирования локально

### :desktop_computer: Поднимите локальную версию базы данных

```commandline
DB_NAME=test DB_USER=test DB_PASSWORD=test DB_PORT=5431 DB_HOST=localhost DB_DRIVER=postgresql docker-compose -f local-dev-database.yml up -d
```

### :desktop_computer: Для локальных тестов понадобится отдельная база данных, потому что фикстуры тестов удаляют все данные из базы для чистоты тестов.

Зайдите в созданный контейнер:

```commandline
docker exec -it local-dev-db-for-testing bash
```

и выполните команды:

```commandline
psql -h localhost -U test
```

```sql
CREATE DATABASE test;
```

### :desktop_computer: Настройте структуру базы

```commandline
DB_NAME=test DB_USER=test DB_PASSWORD=test DB_PORT=5431 DB_HOST=localhost DB_DRIVER=postgresql alembic upgrade head
```

### Пользуйтесь командой миграции:

```commandline
DB_NAME=test DB_USER=test DB_PASSWORD=test DB_PORT=5431 DB_HOST=localhost DB_DRIVER=postgresql alembic revision --autogenerate -m “Оставляйте осмысленное описание изменений”
```