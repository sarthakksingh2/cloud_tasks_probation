
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Shrey27:<db_password>@witty-coder.yg15q.mongodb.net/?retryWrites=true&w=majority&appName=witty-coder"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.todo_db
collection = db["todo_data"]