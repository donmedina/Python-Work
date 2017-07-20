import scrapy

class BlogSpider(scrapy.Spider):
    name = 'brasil'
    start_urls = ['http://g1.globo.com/']

    def parse(self, response):
        for url in response.css('ui li a::attr("href")').re(r'.*/\d\d\d\d/\d\d/$'):
            yield scrapy.Requests(response.urljoin(url), self.parse_titles)

    def parse_titles (self, response):
        for post_title in response.css('div.entries > ul > li a::text').extract():
            yield {'title' : post_title}
