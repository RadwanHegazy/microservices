# Microservices Project
This is a simple implementation for microservices archeticture style "Todo Application" .
I use only python in the services of backend and i use some of its backend frameworks to 
create the system. 

## Installation
```
git clone https://github.com/RadwanHegazy/python-microservices.git
```

```
cd python-microservices
```
---
**1) Run Microservices**
```
pip install -r services\requirements.txt && py services\run_all.py
```
**run_all.py** : this is a python file that run all the microservices in oneline by made thread for each service

**2) Run API Gateway on port 4444**
```
pip install -r api_gateway\requirements.txt && py api_gateway\core\manage.py runserver 4444
```

**3) Run Frontend Server on port 8000**
```
pip install -r frontend\requirements.txt && py frontend\frontend\manage.py runserver
```

### Now You Can Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## Frameworks that i used

### Flask
For fetching all data from the db

### FastAPI
For Retriving data from the db 

### Falcon
For delete data from the db

### Tornado
For updating data on the db

### Bottle
For insert data on the db


## Database
- **MySQL** the main db that all services connected with

## ORM
- **RadawnORM** this is a simple ORM i created it for deling with dbs like sqlite3 and mysql, [see more](https://github.com/RadwanHegazy/RadwanORM/)


## API Gateway
- **Django** i use drf in django to create the rest apis , and connect other services in this gateway.

