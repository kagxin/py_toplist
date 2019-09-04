# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Item
from .mongo import m
from .items import EntryItem


class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):
    """
    将item写入MongoDB
    """

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        if not isinstance(item, EntryItem):
            return item
        collection = m.entry
        data = dict(item)
        collection.update_one({'rank': data['rank'], 'url': data['url']},
                              {'$set': {'target': data['target'], 'title': data['title'],
                                        'release_date': data['release_date']}},
                              upsert=True)
        return item
