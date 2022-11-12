import os 
import pymongo

from dotenv import load_dotenv

load_dotenv()

Secret = os.environ.get('secret')

# MONGO_URI = "mongodb+srv://<USER NAME>:<USER PASSWORD>.mongodb.net/?retryWrites=true&w=majority"
MONGO_URI = Secret
MONGO_CONN = pymongo.MongoClient(MONGO_URI)

def conn_mongodb():
    db = MONGO_CONN.online_store
    return db