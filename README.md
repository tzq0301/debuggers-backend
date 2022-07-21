# Today's Singing Helper (Backend)

## What is in the Project

| file             | usage                                                 |
|------------------|-------------------------------------------------------|
| .env             | contains the properties of the project (maybe secret) |
| config.py        | extracts the settings in the .env                     |
| db.py            | tackles with the database                             |
| db.sql           | the SQL scripts of the MySQL                          |
| main.py          | the entrance of the whole application                 |
| model.py         | contains the models of the application                |
| requirements.txt | the requirements of the Python environment            |


## How to build

* Python 3.8.13
* FastAPI 0.79.0
* pydantic 1.9.1
* PyMySQL 1.0.2 
* SQLAlchemy 1.4.39

```shell
$ pip install -r requirements.txt
```

## How to run

### Prerequisite

You need a file named `.env` like below:

```properties
MYSQL_USERNAME=
MYSQL_PASSWORD=
MYSQL_URL=
MYSQL_DATABASE=
```

`MYSQL_URL` can be the host of the server like `114.14.1.4` (it will use the default port of MySQL, i.e. 3306) or the combination of the host and ip like `114.14.1.4:3310`. 

### Run in Dev mode

```shell
$ uvicorn main:app --reload
```

## How to extract requirements.txt

```shell
$ pip install pipreqs
$ pipreqs . --force
```