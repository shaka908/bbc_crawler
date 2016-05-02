# bbc_crawler
This is a demo for bbc news crawling.



#File Description

django_api: source codes for the RESTful API (Django Rest Framework based)

scrapy_task: source codes to crawl bbc.com through Scrapy

venv: virtual environment setting


# DB Description
Crawled data is in compose mongod and can be read by:

mongodb://public_read:password@aws-us-east-1-portal.11.dblayer.com:27790,aws-us-east-1-portal.10.dblayer.com:11140/bbc

General schema: title, author, division(of author), date, section, content.

#API Description
Here is the accessing API(Deployed with EC2):

http://54.169.211.63:8000/search_or/: return 10 random news

http://54.169.211.63:8000/search_or/key words: return news contains any of the key words (max number of return is 50)

http://54.169.211.63:8000/search_and/: return 10 random news

http://54.169.211.63:8000/search_and/key words: return news contains the key wrods phrase (No. of return: max=50)

http://54.169.211.63:8000/lookup_url/url_name: retrieve news by their url suffix. E.g.: http://54.169.211.63:8000/lookup_url/world-latin-america-36184799

http://54.169.211.63:8000/lookup_date/date_string: retrieve news for specific date. E.g.: http://54.169.211.63:8000/lookup_date/26 April 2016


# Remark
1) The crawling is constrained to bbc.com/news domain. 

2) API search return number limited to 50 to avoid heavy traffic load.
