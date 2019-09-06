# -*- coding: utf-8 -*-
import scrapy
import datetime
from spider.items import EntryItem

class WeixinSpider(scrapy.Spider):
    name = 'weixin'
    allowed_domains = ['weixin.sogou.com']
    start_urls = ['https://weixin.sogou.com/?pid=sogou-wsse-721e049e9903c3a7&kw=']

    def parse(self, response):
        for index, res in enumerate(response.xpath('//ul[@class="news-list"]//h3')):
            title = res.xpath('a/text()').get('')
            url = res.xpath('a/@href').get('')
            item = EntryItem()
            item['target'] = '微信'
            item['title'] = title
            item['rank'] = index + 1
            item['url'] = response.urljoin(url)
            item['release_date'] = datetime.datetime.now()
            yield item
