# trueffelschwein

An example how to set up a Docker based web crawling infrastructure
using Scrapy and MongoDB.

This requires:

* `docker`
* `docker-compose`

## Setup

`$> docker-compose build`

## Run on Dockerhost

`$> docker-compose up`

## Scale crawler containers

`$> docker-compose scale crawler=<num>`

## Stop crawlers

`$> docker-compose stop crawler` or `$> docker-compose scale crawler=0`

## Stop crawler database

`$> docker-compose stop crawlerstore`

## Stop everything

`$> docker-compose stop`

## Start everything (again)

`$> docker-compose start`

## Remove every (stopped) container

`$> docker-compose rm`
