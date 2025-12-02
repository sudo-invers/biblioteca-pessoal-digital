from fastapi import FastAPI
from program.controller.BaseController import router as publication_router

app = FastAPI()

app.include_router(publication_router)
