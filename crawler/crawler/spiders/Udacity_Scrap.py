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
    name = "Udacity"
    allowed_domains = ["in.udacity.com"]
    
    def __init__(self, category=None, *args, **kwargs):
        self.driver = webdriver.Firefox()
        super(SeleniumCrawlerSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://in.udacity.com/courses/all']
        
        self.log("Init finished")

    def parse_trip_items(self):
        self.log("starting to parse divs")
        
        items = []
        links = self.driver.find_elements_by_css_selector('.course-summary-card')


        for link in links:
            item = self.TripItem()
            item['title'] = link.find_element_by_css_selector('.col-sm-8 .h-slim a').text
            item['link'] = link.find_element_by_css_selector('.col-sm-8 .h-slim a').get_attribute('href')
            item['detail'] = link.find_element_by_css_selector('.csdisp').text         
            item['professor'] = ''
            items.append(item)
                    
        return items

    
    def parse(self, response):
        self.driver.get(response.url)
        allitems = self.parse_trip_items()
        # i=2
        # while i<114:
        #     items=self.parse_trip_items()
        #     for j in items:
        #         allitems.append(j)
        #     try: 
        #         next_url = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/ul/li['+ str(i) +']')
        #         next_url.click()
        #         time.sleep(5)
        #         if i%5==0:
        #             next_page = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/ul/div[2]')
        #             next_page.click()
        #         i = i+1
        #     except:
        #         break


        return allitems


    
    
    class TripItem(Item):
        link = Field()
        title = Field()
        institute = Field()
        professor = Field()