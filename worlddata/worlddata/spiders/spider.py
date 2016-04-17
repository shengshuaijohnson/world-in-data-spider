__author__ = 'Administrator'
# -*- coding: UTF-8 -*-
from scrapy.spider import Spider
import scrapy
from worlddata.items import Country



class CountrySpider(Spider):
    name = "world"
    start_urls = ["http://ourworldindata.org/grapher/view/132?tab=map"]
    def load_item(self,d):
        return d
    def parse(self,response):
        yield scrapy.Request(
            url="http://ourworldindata.org/grapher/build/js/data/world.ids.json",
            callback=self.parse_next,
            method='GET'
            )
    def parse_next(self,response):
        print "**********************************************************************"
        items=[]
        text=response.body
        item=Country()
        item["text"]=text
        return item
        """
        for i in text:
            item=Country()

            item["text"]=i
            items.append(item)
        for d in items:
            yield self.load_item(d)
        return
        """