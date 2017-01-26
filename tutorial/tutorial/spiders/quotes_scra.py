import scrapy

class QuotesSpider(scrapy.Spider):
	name = "quotes1"
	start_urls = ['http://quotes.toscrape.com/page/1/',]
	def parse(self, response):
		for quote in response.css('div.quote'):
			print(type(quote.css('span.text::text').extract_first()))
			yield {
				'text': quote.css('span.text::text').extract_first(),
			}