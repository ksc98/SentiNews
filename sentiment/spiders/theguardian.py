import scrapy
import logging
import json
from pprint import pprint
from sentiment.items import SentimentItem
from sentiment.nlp import gcp_nlp
from sentiment.mongo_helpers import exists
from cprint import *

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class TheGuardianSpider(scrapy.Spider):
    name = 'theguardian'
    allowed_domains = ['www.theguardian.com']

    start_urls = [
        'https://www.theguardian.com/us-news/2021/feb/12/john-weaver-lincoln-project-allegations',
        'https://www.theguardian.com/us-news/2021/feb/12/mike-pence-nuclear-football-capitol-riot',
        'https://www.theguardian.com/us-news/2021/feb/14/toxic-plant-chicago-minority-neighborhood-hunger-strike',
        'https://www.theguardian.com/us-news/2021/feb/15/pelosi-congress-commission-investigate-capitol-riot'
    ]

    def start(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = SentimentItem()
        title = response.xpath('//title//text()').get()
        content = response.xpath('//p//text()').extract()

        # print title of article
        logging.debug(b_cyan(f'"{title}"'))

        if (item := exists(title=title, collection=self.name)):
            logging.debug(
                b_magenta('Article exists in database, skipping processing...'))
            logging.debug(yellow(f"_id: {item['_id']}"))
        else:
            logging.debug(
                green('Article not found in database, proceeding with processing...'))
            content = ' '.join(content)
            logging.debug(green(f'Sending article to GCP NLP...'))
            nlp = gcp_nlp(content)
            sentiment = dict(nlp.get('documentSentiment', {}))
            yield (item := {
                'provider': self.name,
                'title': title,
                'body': content,
                'sentiment': sentiment
            })
