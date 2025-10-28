# gRPC Service Project

Простой gRPC сервис с клиентом и сервером на Python.

## Быстрый старт

```bash
# 1. Создание и активация виртуального окружения
python -m venv .venv
.\.venv\Scripts\activate

# 2. Установка зависимостей
pip install -r requirements.txt

# 3. Запуск сервера
python -m grpc_server

# 4. В другом терминале - запуск клиента
python grpc_client.py
```

## Установка и настройка protoc

### 1. Установка protoc (Windows)

1. Скачайте последнюю версию protoc с [официальной страницы релизов](https://github.com/protocolbuffers/protobuf/releases)
2. Скачайте архив `protoc-<version>-win64.zip`
3. Распакуйте архив в `C:\tools\protoc\`
4. Добавьте путь в переменную среды PATH:
   - Откройте "Система" → "Дополнительные параметры системы" → "Переменные среды"
   - Найдите переменную PATH → "Изменить" → "Новая"
   - Добавьте: `C:\tools\protoc\bin`
5. Проверьте установку:
   ```cmd
   protoc --version