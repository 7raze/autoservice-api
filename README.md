# Car Service API

Небольшой API для автосервиса на Django REST Framework.

Проект сделан для работы с клиентами, машинами и заявками на ремонт.

## Что есть в проекте

В проекте есть три основные сущности:

- клиенты;
- автомобили;
- заявки на обслуживание.

Через API можно:

- получать список записей;
- получать одну запись по id;
- фильтровать данные через параметры в URL;
- создавать одну запись;
- создавать несколько записей сразу;
- обновлять одну запись;
- обновлять несколько записей;
- удалять одну запись;
- удалять несколько записей.

## Использованные технологии

- Python
- Django
- Django REST Framework
- drf-spectacular
- SQLite

## Как запустить

Сначала нужно скачать проект:

```bash
git clone ссылка_на_репозиторий
cd autoservice_api

## Документация

Swagger доступен по адресу:

http://127.0.0.1:8000/api/docs/

## Эндпоинты

### Clients

- GET /api/v1/clients/ — список клиентов
- GET /api/v1/clients/{id}/ — один клиент
- GET /api/v1/clients/?full_name=Иван — фильтр по имени
- POST /api/v1/clients/ — создание клиента или нескольких клиентов
- PATCH /api/v1/clients/{id}/ — обновление клиента
- PATCH /api/v1/clients/batch_update/ — массовое обновление
- DELETE /api/v1/clients/{id}/ — удаление клиента
- DELETE /api/v1/clients/batch_delete/?ids=1,2,3 — массовое удаление

### Cars

- GET /api/v1/cars/ — список автомобилей
- GET /api/v1/cars/{id}/ — один автомобиль
- GET /api/v1/cars/?brand=Toyota — фильтр по марке
- GET /api/v1/cars/?client=1 — фильтр по клиенту
- POST /api/v1/cars/ — создание автомобиля или нескольких автомобилей
- PATCH /api/v1/cars/{id}/ — обновление автомобиля
- PATCH /api/v1/cars/batch_update/ — массовое обновление
- DELETE /api/v1/cars/{id}/ — удаление автомобиля
- DELETE /api/v1/cars/batch_delete/?ids=1,2,3 — массовое удаление

### Service Requests

- GET /api/v1/service-requests/ — список заявок
- GET /api/v1/service-requests/{id}/ — одна заявка
- GET /api/v1/service-requests/?status=new — фильтр по статусу
- GET /api/v1/service-requests/?car=1 — фильтр по автомобилю
- POST /api/v1/service-requests/ — создание заявки или нескольких заявок
- PATCH /api/v1/service-requests/{id}/ — обновление заявки
- PATCH /api/v1/service-requests/batch_update/ — массовое обновление
- DELETE /api/v1/service-requests/{id}/ — удаление заявки
- DELETE /api/v1/service-requests/batch_delete/?ids=1,2,3 — массовое удаление