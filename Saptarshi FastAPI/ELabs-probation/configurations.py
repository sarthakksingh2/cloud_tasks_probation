
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Sappy:Saptarshi%40123@fastapi.n5qe3.mongodb.net/?retryWrites=true&w=majority&appName=FastAPI"


client = MongoClient(uri, server_api=ServerApi('1'))

db = client.todo.db

collection=db["todo_data"]

