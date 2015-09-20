# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class CrawlerItem(scrapy.Item):
    url = Field()
    html_title = Field()
    html_h1 = Field()
    html_h2 = Field()
    html_h3 = Field()
    html_h4 = Field()
    html_h5 = Field()
    html_h6 = Field()
    html_p = Field()
    html_a = Field()
