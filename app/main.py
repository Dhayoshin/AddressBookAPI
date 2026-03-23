from fastapi import FastAPI
from .database import Base, engine
from .routes import router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book API")

app.include_router(router)


@app.get("/")
def root():
    """Root endpoint to check if the API is running."""
    return {"message": "Address Book API is running"}