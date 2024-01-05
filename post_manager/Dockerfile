FROM python:3.10-alpine AS builder

WORKDIR /tmp

COPY pyproject.toml poetry.lock ./

RUN apk add build-base libffi-dev

RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* ./
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes


FROM python:3.10-alpine
WORKDIR /code

COPY --from=builder /tmp/requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 80

CMD ["uvicorn", "post_manager.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
