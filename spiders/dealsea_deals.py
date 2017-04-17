import scrapy

class CouponSpider(scrapy.Spider):
    name = "coupon_dealsea"
    page_number = 1

    def increment_page_number(self):
        self.page_number = self.page_number + 1
        return self.page_number

    def start_requests(self):
        urls = [
            'https://dealsea.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for coupons in response.xpath('//div[@class="dealbox"]'):
        # for coupons in response.xpath('//div[@class="pages"]'):
            # if coupons.css('posttext').xpath('./ul').extract() is None:
            #     des = coupons.css('posttext').xpath('./a/text()').extract() +
            #           coupons.css('.posttext').xpath('./text()').extract()
            if coupons.xpath('./div[@class="dealcontent"]/div[@class="posttext"]/a/@href').extract_first() is not None:
                yield{
                    'item': coupons.xpath('./div[@class="dealcontent"]/strong/a/text()').extract(),
                    'imag': coupons.xpath('./div[@class="prodimage"]/a/img/@src').extract(),
                    'link': "http://dealsea.com" + coupons.xpath('./div[@class="dealcontent"]/div[@class="posttext"]/a/@href').extract_first(),
                    'description': coupons.xpath('./div[@class="dealcontent"]/div[@class="posttext"]/a/text()').extract() +
                                coupons.xpath('.//div[@class="posttext"]/text() | .//div[@class="posttext"]/b/text() | .//div[@class="posttext"]/strong/text()').extract() +
                                coupons.xpath('.//div[@class="posttext"]/ul/li/a/text() | .//div[@class="posttext"]/ul/li/text() | .//div[@class="posttext"]/ul/li/b/text() | .//div[@class="posttext"]/ul/li/strong/text()').extract(),
                    'feature': " "
                }
            else:
                pass
        
        next_page_number = str(self.increment_page_number())
        next_page = "http://dealsea.com/" + "?" + "page=" + next_page_number 
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)