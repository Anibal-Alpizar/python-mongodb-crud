from fastapi import FastAPI
from routes.user import router as UserRouter

app = FastAPI() 

app.include_router(UserRouter)