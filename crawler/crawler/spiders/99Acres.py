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
    name = "99Acres"
    allowed_domains = ["www.99acres.com"]
    
    def __init__(self, category=None, *args, **kwargs):
        self.driver = webdriver.Firefox()
        super(SeleniumCrawlerSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.99acres.com/']
        
        self.log("Init finished")

    def parse_trip_items(self):
        self.log("starting to parse divs")
        
        items = []
        links = self.driver.find_elements_by_css_selector('.srpWrap')


        for link in links:
            item = self.TripItem()
            item['title'] = link.find_element_by_css_selector('.wrapttl .srpttl a').get_attribute('title')
            item['link'] = link.find_element_by_css_selector('.wrapttl .srpttl a').get_attribute('href')
            try:
                item['price'] = link.find_elements_by_css_selector('.wrapttl .srpttl b')[1].text
            except:
                item['price'] = 'Price on demand'
            details = link.find_element_by_css_selector('.srpDetail .hm10').text
            item['detail'] = details.split(' : ')[1][:-11]
            item['postingDate'] = details.split(' : ')[2]
            featuresList = link.find_elements_by_css_selector('.srpDetail .srpDataWrap .iconDiv i')
            featuresObject = (i.get_attribute('value') for i in featuresList) 
            list_feature = []
            for i in featuresObject:
                print(i)
                list_feature.append(i)
            item['features'] = list_feature
            pos = link.find_element_by_css_selector('.srpWrap .wrapttl i').get_attribute('data-maplatlngzm')
            item['position'] = pos.split(',')[0]+','+pos.split(',')[1]
            items.append(item)
                    
        return items

    
    def parse(self, response):
        self.driver.get(response.url)
        allitems = []
        i=1
        while i<3:
            items=self.parse_trip_items()
            for j in items:
                allitems.append(j)
            try: 
                next_url = self.driver.find_element_by_xpath('//*[@id="results"]/div[1]/div[34]/a[' + str(i) + ']')
                next_url.click()
                time.sleep(3)
                i = i+1
            except:
                break


        return allitems


    
    
    class TripItem(Item):
        link = Field()
        title = Field()
        institute = Field()
        professor = Field()