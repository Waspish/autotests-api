# Api Automation Project

## Предусловия

```bash
# 1. Создание и активация виртуального окружения
python -m venv .venv
.\.venv\Scripts\activate

# 2. Установка зависимостей
pip install -r requirements.txt
```


## Быстрый старт для gRPC сервиса

```bash
# 1. Переходв папку gRPC
cd .\gRPC\

# 2. Запуск сервера
python -m grpc_server

# 3. В другом терминале - запуск клиента
python -m grpc_client
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
   
## Быстрый старт для WebSocket сервиса

```bash
# 1. Переходв папку WebSocket
cd .\WebSocket\  

# 2. Запуск сервера
python -m websocket_server

# 3. В другом терминале - запуск клиента
python -m websocket_client
```

## Быстрый старт для TCP-IP сервиса

```bash
# 1. Переходв папку WebSocket
cd .\TCP-IP\  

# 2. Запуск сервера
python -m tcp_server

# 3. В другом терминале - запуск клиента
python -m tcp_client
```

## Все остальное (в соответсвующих папках)

```bash
python -m {название_файла}
```