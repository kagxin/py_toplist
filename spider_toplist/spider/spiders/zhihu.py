# -*- coding: utf-8 -*-
import scrapy
from spider.items import EntryItem
import datetime
import json


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50']

    def parse(self, response):
        hots = json.loads(response.text)
        for index, hot in enumerate(hots['data']):
            item = EntryItem()
            item['target'] = '知乎'
            item['title'] = hot['target']['title']
            item['rank'] = index + 1
            item['url'] = hot['target']['url']
            item['release_date'] = datetime.datetime.now()
            yield item
