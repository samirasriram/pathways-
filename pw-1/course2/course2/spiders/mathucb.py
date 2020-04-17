# -*- coding: utf-8 -*-
import scrapy


class MathucbSpider(scrapy.Spider):
    name = 'mathucb'
    allowed_domains = ['math.berkeley.edu']
    start_urls = ['https://math.berkeley.edu/~xuwenzhu/classes/Berkeley/2019Spring104/index.html']

    def parse(self, response):
        title = response.css('title::text').get()
        section1 = response.css('p::text')[1].get()
        section2 = response.css('p::text')[2].get()
        instructorname = response.css('p::text')[7].get()
        office = response.css('p::text')[8].get()
        officehour = response.css('p::text')[9].get()
        examlectures = response.css('body::text').getall()

        scraped_info = {
            'Page Title' : title,
            'Sections ' : section1 + section2,
            'Instructor Information' : instructorname + office + officehour,
            'Exams and Lectures' : examlectures,

        }

        yield scraped_info