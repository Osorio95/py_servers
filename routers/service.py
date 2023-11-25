import docker
from fastapi import APIRouter

router = APIRouter()
client = docker.from_env()

client.images.pull("alpine:latest")

@router.post('/docker')
async def docker_create():
    container = client.containers.create("alpine", "echo hello world", detach=True)

    container.start()

    return {'message': f'Container id: {container.id}, created successfully!'}

@router.get("/docker")
async def docker_list():
    containers = client.containers.list(all=True)
    container_ids = [container.id for container in containers]
    
    return {"containers": container_ids}

@router.get("/docker/{id}")
async def docker_logs(id: str):
    container = client.containers.get(id)
    logs = container.logs()

    return {"logs": logs}

@router.delete("/docker/{id}")
async def docker_remove(id: str):
    container = client.containers.get(id)
    
    container.stop()
    container.remove()
    
    containers = client.containers.list(all=True)
    container_ids = [container.id for container in containers]
    
    return {"containers": container_ids}
