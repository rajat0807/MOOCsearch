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
    name = "Coursera"
    allowed_domains = ["www.coursera.org"]
    
    def __init__(self, category=None, *args, **kwargs):
        self.driver = webdriver.Firefox()
        super(SeleniumCrawlerSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://www.coursera.org/courses?languages=en&start=0']
        
        self.log("Init finished")

    def parse_trip_items(self):
        self.log("starting to parse divs")
        
        items = []
        links = self.driver.find_elements_by_css_selector('.rc-OfferingCard')


        for link in links:
            item = self.TripItem()
            item['title'] = link.find_element_by_css_selector('.color-primary-text').text
            item['link'] = link.get_attribute('href')
            item['institute'] = link.find_element_by_css_selector('.text-light').text         
            try:
                item['detail'] = link.find_element_by_css_selector('.specialization-course-count').text
            except:
                item['detail'] = ''
            items.append(item)
                    
        return items

    
    def parse(self, response):
        self.driver.get(response.url)
        i=1
        allitems = []
        while True:
            items=self.parse_trip_items()
            for j in items:
                allitems.append(j)    
            self.driver.find_element_by_css_selector('i.cif-chevron-right').click()
            time.sleep(5)
            if i==84:
                break
            i=i+1

        
            


        return allitems


    
    
    class TripItem(Item):
        link = Field()
        title = Field()
        institute = Field()
        detail = Field()