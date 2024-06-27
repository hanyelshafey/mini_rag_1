from fastapi import FastAPI ,APIRouter
import os 
base_router = APIRouter(
    prefix='/api/v1',
    tags=['api-v1'],
)

@base_router.get('/')
async def welcom():
    APP_NAME=os.getenv("APP_NAME")
    APP_version=os.getenv("APP_version")
    return{"APP_NAME":APP_NAME,'APP_version':APP_version}

