# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import SpiderPexItem


class PexSpider(CrawlSpider):
    name = 'pex'
    allowed_domains = ['www.pexels.com']
    start_urls = ['https://www.pexels.com/photo/vehicle-on-road-along-green-grass-during-night-714023/']

    rules = (
        Rule(LinkExtractor(allow=r'/photo/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = SpiderPexItem()
        img_url = response.xpath("//img[@class='image-section__image js-photo-zoom']/@src").extract_first()
        if img_url is not None:
            if "?" in img_url:
                new_img_url = img_url.split("?")[0]
            else:
                new_img_url = img_url
            i['img_url'] = new_img_url
            print('crawl img success:'+new_img_url)
            return i
