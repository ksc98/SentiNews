import pymongo
import logging
import time
from cprint import *
from pymongo.errors import ConnectionFailure
import sentiment.settings as settings

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# t/f db status
def check_connection(client):
    try:
        client.admin.command('ismaster')
        logging.debug(b_green("Successfully connected to Mongo db!"))
        return True
    except ConnectionFailure:
        logging.debug(underline(b_red(
            f"Could not connect to Mongo DB ({settings.MONGO_SERVER}:{settings.MONGO_PORT})")))
        return False


def connect():
    global client
    logging.debug(b_blue(
        f'Attempting to connect to MongoDB...'))
    client = pymongo.MongoClient(
        str(settings.MONGO_SERVER),
        int(settings.MONGO_PORT),
        serverSelectionTimeoutMS=2500
    )
    status = check_connection(client)
    return status, client


# check if item exists in database
def exists(title=None, collection=None):
    db = client[settings.MONGO_DATABASE][collection]
    if title:
        title_exist = db.find_one({'title': title})
        return title_exist or None
