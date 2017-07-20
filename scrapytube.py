import scrapy
from scrapy.loader import ItemLoader

class YoutubeVideo(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    views = scrapy.Field()
    up = scrapy.Field()

class YoutubeChannelLister(scrapy.Spider):
    name = 'youtube-channel-lister'
    youtube_channel = 'UCnnAzRbUm_6mSqyqAJSkc_A'
    start_urls = ['https://www.youtube.com/channel/%s/videos' % youtube_channel]

    def parse(self, response):
        for sel in response.css("ul#channels-browse-content-grid > li"):
            loader = ItemLoader(YoutubeVideo(), selector=sel)

            loader.add_xpath('link', './/h3/a/@href')
            loader.add_xpath('title', './/h3/a/text()')
            loader.add_xpath('views', ".//ul/li[1]/text()")
            loader.add_xpath('up', ".//ul/li[2]/text()")


            yield loader.load_item()

