# -*- coding: utf-8 -*-
import scrapy
import datetime
from spider.items import EntryItem


class V2exSpider(scrapy.Spider):
    name = 'v2ex'
    allowed_domains = ['v2ex.com']
    start_urls = ['https://www.v2ex.com/?tab=hot']

    def parse(self, response):
        for index, res in enumerate(response.xpath('//div[@class="box"]/div[contains(@class,"item")]')):
            url = res.xpath('table//span[@class="item_title"]/a/@href').get('')
            title = res.xpath('table//span[@class="item_title"]/a/text()').get('')
            item = EntryItem()
            item['target'] = 'v2ex'
            item['title'] = title
            item['rank'] = index + 1
            item['url'] = response.urljoin(url)
            item['release_date'] = datetime.datetime.now()
            yield item
