# https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import logging
import sys
from cprint import *
from sentiment.mongo_helpers import check_connection
from sentiment.mongo_helpers import connect
import sentiment.settings as settings

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class SentimentPipeline:
    def process_item(self, item, spider):
        logging.debug(underline(b_red(f"process_item in sentiment pipeline")))
        return item


class MongoPipeline:
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_server=crawler.settings.get('MONGO_SERVER'),
            mongo_db=crawler.settings.get('MONGO_DATABASE'),
            mongo_port=crawler.settings.get('MONGO_PORT'))

    # initialize mongo pipeline
    def __init__(self, mongo_server, mongo_db, mongo_port):
        logging.debug(b_yellow(f'Initializing MongoDB Pipeline...'))
        logging.debug(b_yellow(f'\tdb -> {b_magenta(mongo_db)}'))
        self.item_counter = 0
        logging.debug(
            b_yellow(f'\turi -> {b_magenta(mongo_server)}:{b_magenta(mongo_port)}'))
        self.status, self.client = connect()
        if not self.status:
            sys.exit(1)
        self.db = self.client[mongo_db]


    # collection name = spider.name
    def open_spider(self, spider):
        logging.debug(b_green(f'Using collection "{spider.name}"'))
        self.collection = self.db[spider.name]

    # finished with spider
    def close_spider(self, spider):
        logging.debug(b_green(f'Stored {self.item_counter} articles'))
        logging.debug(b_yellow(f'Closing MongoDB Pipeline...'))
        self.client.close()

    # if spider yields an item, store as document in db
    def process_item(self, item, spider):
        collection = self.collection
        logging.debug(green('Inserting item into collection...'))
        collection.insert(dict(item))
        self.item_counter += 1
        logging.debug(
            green("TheGuardian article successfully addeded to MongoDB!"))
        return item
