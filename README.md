# Тестовой задание Python (Kanalservis)

## Краткое описание
Скрипт парсит экселевский гугл [документ](https://docs.google.com/spreadsheets/d/1qqrEwDercKCBlX6XcZRPA7Tn-OBsfMUh0SOllBQUGdI/edit#gid=0)
и обновляет состояние базы данных. Помимо этого в скрипте используется телеграм бот. Чтобы он отработал корректно
перед запуска скрипта необходимо начать диалог с [ботом](https://t.me/kanalservis_task_bot).

## Первичная настройка

Сперва необходимо в корневой папке создать файл `.env` с переменными окружения.

    DB_USER = <имя_пользователя>
    DB_PASSWORD = <пароль>
    DB_HOST = <имя_хоста>
    DB_PORT = <порт>
    DB_NAME = <название_базы>
    TG_BOT_TOKEN = <токен_бота_телеграм>
    TG_CHAT_ID = <id_чата_телеграм>
    SPREADSHEET_TABLE_ID = <id_документа_в_гугл>

Можно использовать файл `.env.example`, предварительно переименовав его в `.env`. Все параметры
можно оставить как есть, кроме `TG_CHAT_ID` - его заменить на свой. Узнать id своего диалога в ТГ
можно у этого [бота](https://t.me/userinfobot)

## Запуск приложения

Чтобы запустить приложение необходимо сперва установить [Docker](https://www.docker.com/)
Запускаем приложение при помощи следующей команды:

    docker-compose up

Иногда происходит так, что приложение flask'а запускается быстрее, чем сама база. Из-за этого контейнер
с приложением делает Exit и перестает работать. 

## Описание API

По урлу /api/stats доступен график стоимости заказов по датам

## Разработчик
Daniil Sobolev - daniil.sob56@gmail.com (telegram: [dansobolev](https://t.me/dansobolev))
