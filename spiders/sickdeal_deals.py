import scrapy

class CouponSpider(scrapy.Spider):
    name = "coupon_slickdeals"
    page_number = 1

    def increment_page_number(self):
        self.page_number = self.page_number + 1
        return self.page_number

    def start_requests(self):
        urls = [
            'https://slickdeals.net/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for coupons in response.xpath('//div[@class="fpGridBox grid  frontpage firedeal"]'):
            yield{
                'item': coupons.xpath('.//a[@class="itemTitle"]/text()').extract(),
                'imag': coupons.xpath('.//div[@class="imageContainer"]/img/@src').extract() +
                        coupons.xpath('.//div[@class="imageContainer"]/img/@data-original').extract(),
                'link': "http://slickdeals.net" + coupons.xpath('.//a[@class="itemTitle"]/@href').extract_first(),
                'description': coupons.xpath('.//div[@class="priceLine"]/@title').extract(),
                'feature': " "
            }
        
        next_page_number = str(self.increment_page_number())
        next_page = "http://slickdeals.net/" + "?" + "page=" + next_page_number 
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)