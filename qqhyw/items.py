# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QqhywItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    main_business = scrapy.Field()
    zip_code = scrapy.Field()
    tel = scrapy.Field()
    mobile = scrapy.Field()
    name = scrapy.Field()
    fox = scrapy.Field()
    address = scrapy.Field()
    context_name = scrapy.Field()

