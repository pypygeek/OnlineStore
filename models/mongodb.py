import pymongo

# MONGO_URI = "mongodb+srv://<USER NAME>:<USER PASSWORD>.mongodb.net/?retryWrites=true&w=majority"
MONGO_CONN = pymongo.MongoClient(MONGO_URI)

def conn_mongodb():
    db = MONGO_CONN.online_store
    return db