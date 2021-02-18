# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy

class SentimentItem(scrapy.Item):
    body = scrapy.Field()
    content = scrapy.Field()
    title = scrapy.Field()
    provider = scrapy.Field()
