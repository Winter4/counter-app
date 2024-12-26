# Развёртывание

## Docker-развёртывание

### Pre-requisites

- Docker & Docker Compose
- make (Unix-builtin)
- python v3.x.x

### Шаги

- `make install` - устанавливаем зависимости
- `make build-image` - собираем образ
- `make compose-up` - поднимаем компоуз с контейнерами

# Результат

Устанавливаем зависимости
![requirements-install](requirements.png)

Собираем образ
![build-image](build.png)

Поднимаем компоуз
![compose](compose.png)

Стучимся в наше приложение
![request](request.png)

Смотрим результат в БД
![adminer](adminer.png)