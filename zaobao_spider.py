import scrapy

class ZaobaoSpider(scrapy.Spider):
    name = 'zaobao'
    start_urls = ["http://stackoverflow.com/questions?sort=votes"]

    def parse(self, response):
        for href in response.css('div.summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_url)

    def parse_url(self, response):
        yield {
            'title': response.css('#question-header h1 a::text').extract(),
            'dt': response.css('p.label-key b a::text').extract(),
            'body': response.css('div.post-text p::text').extract(),
            'link': response.url
        }