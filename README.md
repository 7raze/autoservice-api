# car service api

простое api для автосервиса на django rest framework.

проект нужен для работы с клиентами, машинами и заявками на ремонт.

в api есть 3 сущности: client, car и service request.

client — клиент автосервиса.  
car — машина клиента.  
service request — заявка на ремонт машины.

через api можно получать данные, создавать записи, обновлять их и удалять. также можно работать не только с одним объектом, но и с несколькими сразу.

использованные библиотеки: python, django, django rest framework, drf-spectacular, sqlite. полный список есть в файле requirements.txt.

запуск проекта:

git clone https://github.com/7raze/autoservice-api.git

cd autoservice-api

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

основной адрес api:

http://127.0.0.1:8000/api/v1/

swagger документация:

http://127.0.0.1:8000/api/docs/

endpoints:

clients:

GET /api/v1/clients/ — список клиентов

GET /api/v1/clients/{id}/ — один клиент

GET /api/v1/clients/?full_name=ivan — фильтр по имени

GET /api/v1/clients/?phone=999 — фильтр по телефону

POST /api/v1/clients/ — создать одного или несколько клиентов

PATCH /api/v1/clients/{id}/ — обновить одного клиента

PATCH /api/v1/clients/batch_update/ — обновить несколько клиентов

DELETE /api/v1/clients/{id}/ — удалить одного клиента

DELETE /api/v1/clients/batch_delete/?ids=1,2,3 — удалить несколько клиентов

cars:

GET /api/v1/cars/ — список машин

GET /api/v1/cars/{id}/ — одна машина

GET /api/v1/cars/?brand=toyota — фильтр по марке

GET /api/v1/cars/?model=camry — фильтр по модели

GET /api/v1/cars/?year=2020 — фильтр по году

GET /api/v1/cars/?client=1 — фильтр по клиенту

POST /api/v1/cars/ — создать одну или несколько машин

PATCH /api/v1/cars/{id}/ — обновить одну машину

PATCH /api/v1/cars/batch_update/ — обновить несколько машин

DELETE /api/v1/cars/{id}/ — удалить одну машину

DELETE /api/v1/cars/batch_delete/?ids=1,2,3 — удалить несколько машин

service requests:

GET /api/v1/service-requests/ — список заявок

GET /api/v1/service-requests/{id}/ — одна заявка

GET /api/v1/service-requests/?status=new — фильтр по статусу

GET /api/v1/service-requests/?car=1 — фильтр по машине

GET /api/v1/service-requests/?min_price=1000 — фильтр по минимальной цене

GET /api/v1/service-requests/?max_price=10000 — фильтр по максимальной цене

POST /api/v1/service-requests/ — создать одну или несколько заявок

PATCH /api/v1/service-requests/{id}/ — обновить одну заявку

PATCH /api/v1/service-requests/batch_update/ — обновить несколько заявок

DELETE /api/v1/service-requests/{id}/ — удалить одну заявку

DELETE /api/v1/service-requests/batch_delete/?ids=1,2,3 — удалить несколько заявок

примеры json:

клиент:

{
  "full_name": "ivan petrov",
  "phone": "+79990001122",
  "email": "ivan@example.com"
}

машина:

{
  "client": 1,
  "brand": "toyota",
  "model": "camry",
  "year": 2020,
  "license_plate": "a123bc"
}

заявка:

{
  "car": 1,
  "description": "zamena masla",
  "price": "4500.00",
  "status": "new"
}

