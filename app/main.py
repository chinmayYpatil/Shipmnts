from fastapi import FastAPI
from app.routers import calculate, plan, store
from .routers import auth
# As you create new features, you will import their routers here

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:7016@localhost/fastapi"

app = FastAPI(
    title="Shipmnts API Boilerplate",
    description="A robust boilerplate for the Shipmnts technical interview.",
    version="1.0.0"
)

# Include the authentication router
app.include_router(auth.router)
app.include_router(store.router)
app.include_router(plan.router)
app.include_router(calculate.router)

@app.get("/")
def root():
    """A simple root endpoint to confirm the API is running."""
    return {"message": "Welcome to the Shipmnts API Boilerplate!"}
