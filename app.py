from fastapi import FastAPI
from routes.user import router as UserRouter
from docs.docs import tags_metadata

app = FastAPI(
    title="FastAPI with MongoDB",
    description="This is a simple example of a FastAPI app with MongoDB",
    version="0.1.0",
    openapi_tags=tags_metadata
) 

app.include_router(UserRouter)