# -*- coding: utf-8 -*-
import scrapy
import datetime
from spider.items import EntryItem

class HupuSpider(scrapy.Spider):
    name = 'hupu'
    allowed_domains = ['hupu.com']
    start_urls = ['https://bbs.hupu.com/all-gambia']

    def parse(self, response):
        for index, res in enumerate(response.xpath('//div[@class="bbsHotPit"]//div[@class="list"]/ul/li')):
            url = res.xpath('span[@class="textSpan"]//a/@href').get('')
            title = res.xpath('span[@class="textSpan"]//a/@title').get('')
            item = EntryItem()
            item['target'] = '虎扑'
            item['title'] = title
            item['rank'] = index + 1
            item['url'] = response.urljoin(url)
            item['release_date'] = datetime.datetime.now()
            yield item
