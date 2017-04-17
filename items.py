# -*- coding: utf-8 -*-

# Define here the models for your scraped items

import scrapy


class DealmoonItem(scrapy.Item):
    # define the fields for your item here like:
    discount = scrapy.Field()
    name = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    feature = scrapy.Field()
