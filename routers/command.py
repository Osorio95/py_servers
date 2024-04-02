import docker

from fastapi import APIRouter, status
from models import ContainerCreated, ContainerList, ContainerLogs
from lib.db import docker_collection

router = APIRouter(prefix="/command", tags=["Command"])

@router.post('/run')
async def docker_command(id) -> None:
    user_requested_docker = docker_collection.find_one({"_id": id})
    if (user_requested_docker):
        print(user_requested_docker["docker_id"])
    else:
        print("docker not found")

@router.post('/stop')
async def docker_command(id) -> None:
    user_requested_docker = docker_collection.find_one({"_id": id})
    if (user_requested_docker):
        print(user_requested_docker["docker_id"])
    else:
        print("docker not found")