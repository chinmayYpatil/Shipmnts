from fastapi import FastAPI
from .routers import auth
# As you create new features, you will import their routers here

app = FastAPI(
    title="Shipmnts API Boilerplate",
    description="A robust boilerplate for the Shipmnts technical interview.",
    version="1.0.0"
)

# Include the authentication router
app.include_router(auth.router)

@app.get("/")
def root():
    """A simple root endpoint to confirm the API is running."""
    return {"message": "Welcome to the Shipmnts API Boilerplate!"}
