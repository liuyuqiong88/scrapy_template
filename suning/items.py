# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SuningItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    good_url = scrapy.Field()
    url = scrapy.Field()
    timestamp = scrapy.Field()
    price = scrapy.Field()
    soler = scrapy.Field()
    soler_url = scrapy.Field()
    soler_id = scrapy.Field()
    categate = scrapy.Field()
    # 品牌
    card = scrapy.Field()
    good_name = scrapy.Field()
    good_id = scrapy.Field()

    images = scrapy.Field()

    image_url = scrapy.Field()







    pass
