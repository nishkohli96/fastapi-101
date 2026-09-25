import importlib
import pkgutil

from fastapi import FastAPI

from app import routers

app = FastAPI(
  # As docs & redoc heading and tab title
  title="FastAPI-101",
  description="Learn FastAPI - from basics to advanced.",
  # Default version is 0.1.0
  version="1.1.0"
)


def include_all_routers(app: FastAPI) -> None:
  # Any module in app/routers that defines `router` gets registered.
  for module_info in pkgutil.iter_modules(routers.__path__):
    module = importlib.import_module(f"{routers.__name__}.{module_info.name}")
    if hasattr(module, "router"):
      app.include_router(module.router)


include_all_routers(app)


@app.get("/")
async def root():
  return {"message": "Hello World"}
