FROM python:3.12-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# По умолчанию запускаем entrypoint.sh, его создадим ниже
CMD ["bash", "compose/production/entrypoint.sh"]
