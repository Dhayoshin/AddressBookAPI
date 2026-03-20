from fastapi import FastAPI
from .database import Base, engine
from .routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book API")

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Address Book API is running"}