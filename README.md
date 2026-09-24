# FastAPI - 101

Learn concepts and working of [FastAPI](https://fastapi.tiangolo.com) from basicsto production level code

## Setup

Run the `setup.sh` file which sets up the virtual environment and installs dependencies into it.

```bash
bash setup.sh
```

## Start the server

From the project root:

```bash
uvicorn app.main:app --reload
```

- `app.main` means the Python module: `app/main.py`
- `:app` means the variable:
  ```py
  app = FastAPI()
  ```
- `--reload` means: Restart the development server automatically when your code changes. Don't use in `production` environment.

This runs the server on [http://127.0.0.1:8000](http://127.0.0.1:8000).

**Swagger** - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
**Redoc** - [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
