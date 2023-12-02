from fastapi import FastAPI
from routers.container import router
from routers.command import router_command
from fastapi.staticfiles import StaticFiles
from lib.db import db_client, docker_collection

description = """
py_app let's you create and manage your own minecraft docker container. 🚀
"""

app = FastAPI(
    title="Minecraft Docker Services",
    description=description,
    summary="My favorite app",
    version="0.0.1",
    contact={
        "name": "David Osorio",
        "url": "https://osorio.vercel.app",
        "email": "david.lml.95@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
)

app.include_router(router)
app.include_router(router_command)

app.mount("/static", StaticFiles(directory="static"), name="static")

# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}

# Run server with: uvicorn main:app --reload

# http://localhost:8000/docs
# http://localhost:8000/redoc