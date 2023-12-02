import docker
from fastapi import APIRouter, status
from models import ContainerCreated, ContainerList, ContainerLogs
from lib.db import docker_collection

router_command = APIRouter(prefix="/command", tags=["Command"])

@router_command.post('/run')
async def docker_command(id) -> None:
    user_requested_docker = docker_collection.find_one({"_id": id})
    if (user_requested_docker):
        print(user_requested_docker["docker_id"])
    else:
        print("docker not found")

@router_command.post('/stop')
async def docker_command(id) -> None:
    user_requested_docker = docker_collection.find_one({"_id": id})
    if (user_requested_docker):
        print(user_requested_docker["docker_id"])
    else:
        print("docker not found")