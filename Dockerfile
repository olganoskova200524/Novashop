FROM python:3.12-slim

WORKDIR /app

# системные зависимости для сборки пакетов + postgres client libs
RUN apt-get update \
  && apt-get install -y --no-install-recommends gcc libpq-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# ставим poetry
RUN pip install --no-cache-dir poetry

# важно: копируем только файлы зависимостей (для кеша)
COPY pyproject.toml poetry.lock* /app/

# ставим зависимости (без dev)
# ключевой момент: отключаем venv внутри контейнера
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi --only main

# копируем код
COPY . /app

EXPOSE 8000
