from fastapi import FastAPI

from app.routers import basic

app = FastAPI()
app.include_router(basic.router)


@app.get("/")
async def root():
  return {"message": "Hello World"}
