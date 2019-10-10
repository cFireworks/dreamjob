import scrapy
import pandas as pd

class JobSpider(scrapy.Spider):
    name = 'job'


    # start_urls = ['http://seu.91job.org.cn/campus']

    def start_requests(self):
        urls = [
            "http://seu.91job.org.cn/campus"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_campus)

    def parse_campus(self, response):
        # follow links to author pages
        
        for company_info in response.css('ul.infoList'):
            if company_info:
                filename = 'E:/Workspace/Spider/dreamjob/dreamjob/data/company_info.txt'

                company_url = company_info.css('li.span7 a::attr(href)').get()
                name = company_info.css('li.span7 a::text').get()
                city = company_info.css('li.span1::text').get()
                post_time = company_info.css('li.span4::text').get()

                with open(filename, 'a') as f:
                    f.write('{}\t{}\t{}\t{}\n'.format(company_url, name, city, post_time))


            else:
                print('nothing exist!')


    # def parse_author(self, response):
    #     def extract_with_css(query):
    #         return response.css(query).get(default='').strip()

    #     yield {
    #         'name': extract_with_css('h3.author-title::text'),
    #         'birthdate': extract_with_css('.author-born-date::text'),
    #         'bio': extract_with_css('.author-description::text'),
    #     }