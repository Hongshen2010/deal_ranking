import scrapy
# from dealmoon.items import items

class CouponSpider(scrapy.Spider):
    # AJAXCRAWL_ENABLED = True
    name = "coupon_dealmoon"
    allowed_domains = ['dealmoon.com']
    page_number = 0
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS":{
            'Host': 'www.dealmoon.com',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,en-US;q=0.8,zh;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://www.dealmoon.com/',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Length': '127',
            'Cookie': 'PHPSESSID=664f4f9e2b12d0e80ad9e539786721f1; rip=H',
            'Connection': 'keep-alive'
        }
    }

    def start_requests(self):
        urls = [
            'http://www.dealmoon.com'
        ]
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def increment_page_number(self):
        self.page_number = self.page_number+1
        return self.page_number

    def parse(self, response):

        for coupons in response.xpath('//div[@class="mlist"]'):
            yield{
                'discount': coupons.xpath('.//span[@class="notice_item"]/text()').extract(),
                'item': coupons.xpath('.//span[@class="notice_item"]/following-sibling::*/text()').extract(),
                'imag': coupons.xpath('.//div[@class="img_wrap"]/a/img/@src').extract(),
                'link': "http://www.dealmoon.com/exec/j/?d=" + coupons.xpath('./@data-id').extract_first(),
                'description': coupons.css('.event_statistics').xpath('./ul/descendant::*/text()').extract(),
                'feature': coupons.xpath('.//div[@class="minfor  event_statistics"]/p[last()]/text()').extract()
            }
        
        # next_page_number = str(self.increment_page_number())
        # next_page = "http://www.dealmoon.com/" + next_page_number
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)