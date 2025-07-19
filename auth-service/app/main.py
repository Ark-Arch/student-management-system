# FastAPI app initializer
# helps load all my api routes from a separate file/module

from fastapi import FastAPI
from app.core.config import settings

# import module: that contains my endpoint definitions.
from app.api.v1 import routes 

app = FastAPI(title="Auth Service")

# includes all the endpoints (routes) defined in routes.router into the app
app.include_router(routes.router)