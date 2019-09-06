# -*- coding: utf-8 -*-
import scrapy
from spider.items import EntryItem
import datetime


class QiushibaikeSpider(scrapy.Spider):
    name = 'qiushibaike'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com']

    def parse(self, response):
        for index, res in enumerate(response.xpath('//div[@id="content-left"]/div[contains(@class,"article")]')):
            title = res.xpath('a/div[@class="content"]/span//text()').get('')
            url = res.xpath('a/@href').get('')
            item = EntryItem()
            item['target'] = '糗事百科'
            item['title'] = title
            item['rank'] = index + 1
            item['url'] = response.urljoin(url)
            item['release_date'] = datetime.datetime.now()
            yield item

