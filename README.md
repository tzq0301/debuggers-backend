# Today's Singing Helper (Backend)

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

### Run in Dev mode

```shell
$ uvicorn main:app --reload
```

## How to extract requirements.txt

```shell
$ pip install pipreqs
$ pipreqs . --force
```