import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv, dotenv_values

load_dotenv()

_uri = os.getenv('MONGO_SECRET')

# Create a new client and connect to the server
db_client = MongoClient(_uri, server_api=ServerApi('1'))

_db = db_client["mc-service"]

docker_collection = _db["docker-containers"]

