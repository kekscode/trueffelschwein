# trueffelschwein

An example how to set up a Docker based web crawling infrastructure
using Scrapy and MongoDB.


This requires:

* A dockerhost
* The `docker` command in order to talk to your dockerhost
* The `docker-compose` command
* This repository ;-)

## Setup

`$> docker-compose build`

## Configure

Edit the files in `./config/*.env` to suit your needs

## Run on Dockerhost

Start the whole system with:

`$> docker-compose up`

and check the results in your MongoDB container at `<dockerhost>:27017`.

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
