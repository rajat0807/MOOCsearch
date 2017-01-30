import time
from scrapy.item import Item, Field
from selenium import webdriver
from scrapy.spider import BaseSpider
from scrapy.http import FormRequest
from scrapy import log
from time import strftime
from datetime import timedelta
from datetime import datetime
import datetime
from scrapy.selector import HtmlXPathSelector

class SeleniumCrawlerSpider(BaseSpider):
    name = "lynda"
    allowed_domains = ["www.infiniteskills.com"]
    
    def __init__(self, category=None, *args, **kwargs):
        self.driver = webdriver.Firefox()
        super(SeleniumCrawlerSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.lynda.com/sitemap/courses']
        
        self.log("Init finished")

    def parse_trip_items(self):
        self.log("starting to parse divs")
        
        items = []
        links=self.driver.find_elements_by_css_selector('.grid_4 li a')

        for link in links:

            item = self.TripItem()
            item['title'] = link.text
            item['link'] = link.get_attribute('href')
            items.append(item)
                    
        return items

    
    def parse(self, response):
        self.driver.get(response.url)
        allitems = self.parse_trip_items()
        return allitems


    
    
    class TripItem(Item):
        link = Field()
        title = Field()