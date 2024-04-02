import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv, dotenv_values

load_dotenv()

_uri = "mongodb+srv://admin:aYBJ7elmodAKKDLY@cluster0.7mfh91n.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
db_client = MongoClient(_uri, server_api=ServerApi('1'))

_db = db_client["mc-service"]

docker_collection = _db["docker-containers"]

