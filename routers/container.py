import docker
from fastapi import APIRouter, status
from models import ContainerCreated, ContainerList, ContainerLogs
from models import RequestCreateContainerModel, RequestListContainerModel
from lib.db import docker_collection
from lib.utils import choose_free_port
from utils.container import get_docker_client

router = APIRouter(prefix="/docker", tags=["Docker"])

docker_client = get_docker_client()

docker_client.images.pull("itzg/minecraft-server:latest")

@router.post('/', status_code=status.HTTP_201_CREATED)
async def docker_create(rqCont: RequestCreateContainerModel) -> ContainerCreated:
    """
    The function `docker_create` creates and starts a Docker container running a Minecraft server.
    :return: a dictionary with a single key-value pair. The key is "message" and the value is a string
    that includes the container id and a success message.
    """
    # try:
    sel_port = choose_free_port()
    repeated_query = docker_collection.find_one({"user_id": rqCont.user_id, "name": rqCont.name})
    if repeated_query == None:
        container = docker_client.containers.create(
            "itzg/minecraft-server",
            name=rqCont.name,
            detach=True,
            ports={"25565/tcp": sel_port},
            environment={
                "EULA": "TRUE",
                "VERSION": rqCont.game_version,
                "ENGINE": rqCont.game_engine,
                "MAX_PLAYERS": "10",
                "MOTD": "Welcome to my Minecraft server!",
            }
        )
        docker_collection.insert_one({
            "user_id": rqCont.user_id,
            "name": rqCont.name,
            "port": sel_port,
            "docker_id": container.id,
            "game_version": rqCont.game_version,
            "game_engine": rqCont.game_engine
        })
        container.start()
        return ({"message": "Succesfully created a container and saved it to db"})
    else:
        return ({"message": "You already have a container with that name"})
    # except:
    #     return ({"message": f"There was an error creating the container"})

@router.get("/")
async def docker_list():
    """
    The function `docker_list` returns a dictionary containing a list of container IDs.
    """
    # containers_query = docker_collection.find({"user_id": "01"})
    containers_qty = docker_collection.count_documents({"user_id": "01"})

    return {"containers": containers_qty}

@router.get("/{id}")
async def docker_logs(id: str) -> ContainerLogs:
    """
    The function `docker_logs` retrieves the logs of a Docker container with the specified ID.
    """

    container = docker_client.containers.get(id)
    logs = container.logs()

    return {"logs": logs}

@router.delete("/{id}")
async def docker_remove(id: str):
    """
    The function `docker_remove` stops and removes a Docker container with the given ID and returns a list of the remaining container IDs.
    """

    container = docker_client.containers.get(id)
    
    container.stop()
    container.remove()
    
    containers = docker_client.containers.list(all=True)
    container_ids = [container.id for container in containers]
    
    return {"containers": container_ids}
