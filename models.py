import uuid
from pydantic import BaseModel, Field
from typing import Optional

class RequestContainerModel(BaseModel):
    user_id: str
    name: str
    game_version: str
    game_engine: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "01",
                "name": "minecraft-server",
                "game_version": "1.20.1",
                "game_engine": "FORGE"
            }
        }

class ContainerModel(BaseModel):
    id: str = Field(alias="_id")
    user_id: str
    name: str
    port: str
    docker_id: str
    game_version: str
    game_engine: str
    
    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "user_id": "01",
                "name": "minecraft-server",
                "docker_id": "80f188ff5007faf75c9f78e1555c1f183abb09c00ab1c4a7be2e9c37e5224ad9",
                "game_version": "1.20.1",
                "game_engine": "FORGE"
            }
        }

class ContainerCreated(BaseModel):
    message: str

class ContainerList(BaseModel):
    containers: list[str]

class ContainerLogs(BaseModel):
    logs: list[bytes]