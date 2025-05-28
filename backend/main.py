from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from routes import cow, health

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cow.router, prefix="/cow")
app.include_router(health.router, prefix="/health")