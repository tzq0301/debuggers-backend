# Today's Singing Helper (Backend)

## How to build

* Python 3.8.13
* FastAPI 0.79.0
* pydantic 1.9.1

```shell
$ pip install -r requirements.txt
```

## How to run

### Run in Dev mode

```shell
uvicorn main:app --reload
```

## How to extract requirements.txt

```shell
$ pip install pipreqs
$ pipreqs . --force
```