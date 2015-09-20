FROM python:2
ADD . /crawler
WORKDIR /crawler
RUN pip install -r requirements.txt
CMD [ "scrapy", "crawl", "meepmeep" ]
