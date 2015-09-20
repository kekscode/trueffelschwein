# -*- coding: utf-8 -*-
import scrapy
import os

from scrapy.spiders import CrawlSpider, Rule
from crawler.items import CrawlerItem
from scrapy.linkextractors import LinkExtractor

class MeepmeepSpider(CrawlSpider):
    name = "meepmeep"

    # Read allowed domains and start urls from environment variables
    # Variables are defined with "|" as split character:
    #
    # $> export VARIABLE='first|second|...'
    #
    allowed_domains = os.environ.get('CRAWL_DOMAINS').split('|')
    start_urls = tuple(os.environ.get('CRAWL_URLS').split('|'))

    rules = (
        # Extract links matching .html and parse them
        # with the spider's method parse_page
        #Rule(LinkExtractor(allow=(r'\.html'),), follow=True),
        Rule(LinkExtractor(allow=(r'\.html', ),), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        item = CrawlerItem()
        item['url'] = response.url
        item['html_title'] = response.xpath('//title/text()').extract()
        item['html_h1'] = response.xpath('//h1/text()').extract()
        item['html_h2'] = response.xpath('//h2/text()').extract()
        item['html_h3'] = response.xpath('//h3/text()').extract()
        item['html_h4'] = response.xpath('//h4/text()').extract()
        item['html_h5'] = response.xpath('//h5/text()').extract()
        item['html_h6'] = response.xpath('//h6/text()').extract()
        item['html_a'] = response.xpath('//a[@href]').extract()
        item['html_p'] = response.xpath('//p/text()').extract()
        return item
