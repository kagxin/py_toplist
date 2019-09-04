# -*- coding: utf-8 -*-
import scrapy
from spider.items import EntryItem
import datetime


class QiushibaikeSpider(scrapy.Spider):
    name = 'qiushibaike'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/']
    rank = 1

    def parse(self, response):
        for res in response.xpath('//div[@class="recommend-article"]/ul/li'):
            title = res.xpath('div/a[@class="recmd-content"]/text()').get('')
            url = res.xpath('div/a[@class="recmd-content"]/@href').get('')

            item = EntryItem()
            item['target'] = '糗事百科'
            item['title'] = title
            item['rank'] = self.rank
            item['url'] = response.urljoin(url)
            item['release_date'] = datetime.datetime.now()
            yield item

            self.rank = self.rank + 1
            print(self.rank)
        next_page_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').get()
        if next_page_url:
            yield response.follow(next_page_url, self.parse)
