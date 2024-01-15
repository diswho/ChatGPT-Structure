## Setting up EVN

```sh
python -m venv venv
```

```sh
pip install pipreqs uvicorn httpx python-dotenv python-jose
```

```sh
pipreqs C --force
```

```sh
pip freeze > requirements01.txt
```

```sh
pip install -r requirements.txt
```

```sh
pip install pydantic[dotenv]

```

```sh
pip uninstall
```

## Run App

```sh
uvicorn app.main:app --reload
```

## Run Test

```sh
pip install pytest
```

```sh
pytest
```

## initialize database

```sh
python init_db.py
```
