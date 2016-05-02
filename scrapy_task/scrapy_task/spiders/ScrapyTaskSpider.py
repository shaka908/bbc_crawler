import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_task.items import ScrapyTaskItem

class ScrapyTaskSpider(CrawlSpider):
    name = 'ScrapyTask'
    # allowed_domains = 'bbc.com'
    start_urls = [
            'http://www.bbc.com/',
            ]

    rules = (Rule(LinkExtractor(allow=('http://www\.bbc\.com/news/\w*')),
        callback="parse_obj", follow= True),)



    def parse_obj(self, response):
        item = ScrapyTaskItem()
        item['url'] = response.url
        item['body'] = response.body
        # item['desc'] = response.url
        print(response.url)
        return item
