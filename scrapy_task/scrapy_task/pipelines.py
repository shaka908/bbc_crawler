# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings

from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch

import re


class MongoPipeline(object):
    collection_name = 'scrapy_items'



    def __init__(self):
        # connection = pymongo.MongoClient(
        #     settings['MONGO_SERVER'],
        #     settings['MONGO_PORT']
        # )
        client = pymongo.MongoClient(
            settings['MONGO_URI']
        )
        db = client[settings['MONGO_DB']]
        self.collection = db[settings['MONGO_COLLECTION']]
        self.es = Elasticsearch('https://test_ivan:11111111@aws-us-east-1-portal10.dblayer.com:11141/')


    def process_item(self, item, spider):
        # self.collection.insert(dict(item))
        if '?' in item['url']:
            return item
        elif not re.search(r'\d+$', item['url']):
            return item
        elif item['body']:
            soup = BeautifulSoup(item['body'], 'html.parser')
            story = soup.find('div', {'class':'story-body'})

            if story:
                # type 1
                type1 = story.find('div', {'class':'map-body'})
                byline = False
                mini_info = False

            if story and not type1:
                title = story.find('h1', {'class':'story-body__h1'})
                byline = story.find('div', {'class':'byline'})
                if byline:
                    author = byline.find('span', {'class':'byline__name'})
                    division = byline.find('span', {'class':'byline__title'})
                mini_info = story.find('div',
                    {'class':'story-body__mini-info-list-and-share'})
                if mini_info:
                    datetime = mini_info.find('div')['data-datetime']
                    section = mini_info.find('a',
                        {'class':'mini-info-list__section'})
                content = story.find('div', {'class':'story-body__inner'})
            elif story and type1:
                title = story.find('h1', {'class':'story-body__h1'})
                datetime = story.find('p', {'class':'date date--v1'})
                if datetime:
                    datetime = datetime.get_text()
                content = story.find('div', {'class':'map-body'})
            if story:
                # extract the text from each element
                result = {}
                # result = {'url':item['url']}
                if title:
                    result['title'] = title.get_text()
                if byline and author:
                    result['author'] = author.get_text()
                if byline and division:
                    result['division'] = division.get_text()
                if mini_info and datetime:
                    result['datetime'] = str(datetime)
                if mini_info and section:
                    result['section'] = section.get_text()
                if content:
                    result['content'] = content.get_text()
                #for x in stories:
                if result:
                    result['url']=item['url']
                    # self.collection.insert(result)
                    self.collection.update({'url':result['url']}, result,
                        upsert=True)
                    self.es.index(index="bbc", doc_type='news', body=result)

        return item
