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
    name = "Spider"
    allowed_domains = ["nptel.ac.in"]
    
    def __init__(self, category=None, *args, **kwargs):
        self.driver = webdriver.Firefox()
        super(SeleniumCrawlerSpider, self).__init__(*args, **kwargs)
        
        self.start_urls = ['http://nptel.ac.in/course.php']

        self.log("Init finished")

    def parse_trip_items(self):
        self.log("starting to parse divs")
        
        items = []
        links = self.driver.find_elements_by_css_selector('#overallcs .individualcourse .csinfo .csname i a')


        for link in links:
            item = self.TripItem()
            item['link'] = link.get_attribute('href')
            item['text'] = link.text
            items.append(item)
                    
        return items

    
    def parse(self, response):
        self.driver.get(response.url)
        
        allitems = []
        i=2
        while i<113:
            items=self.parse_trip_items()
            for j in items:
                allitems.append(j)
            try: 
                next_url = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/ul/li['+str(i)+']')
                next_url.click()
                if i%5==0:
                    next_page = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/ul/div[2]')
                    next_page.click()
                time.sleep(5)
                i = i+1
            except:
                break


        return allitems

    
    
    class TripItem(Item):
        link = Field()
        text = Field()