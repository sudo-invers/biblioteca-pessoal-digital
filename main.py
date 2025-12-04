import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from program.databases.DatabaseConnection import RepositoryConnection

# Importing the routers directly
from program.controller.BookController import router as book_router
from program.controller.MagazineController import router as magazine_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("--- STARTING DATABASE ---")
    try:
        # Initialize database connection
        RepositoryConnection()
        print("--- DATABASE CONNECTED ---")
    except Exception as e:
        print(f"--- DATABASE ERROR: {e} ---")
    yield
    print("--- SHUTTING DOWN ---")


app = FastAPI(title="Library Manager", lifespan=lifespan)

# Register Routers
app.include_router(book_router)
app.include_router(magazine_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
