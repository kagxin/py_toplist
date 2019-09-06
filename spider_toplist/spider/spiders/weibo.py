# -*- coding: utf-8 -*-
import scrapy
import datetime
from spider.items import EntryItem

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.com']
    start_urls = ['https://s.weibo.com/top/summary']

    def parse(self, response):
        for index, res in enumerate(response.xpath('//table//td[@class="td-02"]')):
            title = res.xpath('a//text()').get('')
            url = res.xpath('a/@href').get('')
            item = EntryItem()
            item['target'] = '微博'
            item['title'] = title
            item['rank'] = index + 1
            item['url'] = response.urljoin(url)
            item['release_date'] = datetime.datetime.now()
            yield item
