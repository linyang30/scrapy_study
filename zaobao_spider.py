import scrapy

class ZaobaoSpider(scrapy.Spider):
    name = 'zaobao'
    start_urls = ['http://www.zaobao.com.sg/special/report/politic/fincrisis']

    def parse(self, response):
        for href in response.css('div.ds-1col a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_url)

    def parse_url(self, response):
        yield {
            'title': response.css('div.body-content h1::text').extract(),
            'dt': response.css('span.datestamp::text').extract(),
            'body': response.css('div.article-content-container p::text').extract(),
            'link': response.url
        }