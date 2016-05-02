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

#API
Here is the accessing API:
http://54.169.211.63:8000/search_or/ 

http://54.169.211.63:8000/search_or/
http://54.169.211.63:8000/search_or/
http://54.169.211.63:8000/search_or/
http://54.169.211.63:8000/search_or/
http://54.169.211.63:8000/search_or/


# Remark
1) The crawling is constrained to bbc.com/news domain. 
2) API search return number limited to 50 to avoid heavy traffic load.
