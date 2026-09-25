from fastapi import FastAPI

from app.routers import basic, mutation

app = FastAPI(
  # As docs & redoc heading and tab title
  title="FastAPI-101",
  description="Learn",
)
app.include_router(basic.router)
app.include_router(mutation.router)


@app.get("/")
async def root():
  return {"message": "Hello World"}
