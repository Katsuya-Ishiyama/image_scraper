# image_scraper
## Overview
image_scraper, based on scrapy, has been designed to download images of
Keyakizaka46.  
Yahoo Japan is used for the search engine.

## Requirements
python 3.5 or higher  
Scrapy 1.4.0 or higher

## Usage
First of all, you must move to `image_scraper`.
```bash
$ cd image_scraper
```
If you would like to get the images of 1 member, you are
able to execute the following code.
```bash
$ scrapy crawl yahoo_image -a query={your query} -a member_id={id of member}
```
image_scraper will make directories `download/{id of member}` and save downloaded images into there.

If you would like to get the images over all members,
you can run `execute_crawl.sh` like this:
```bash
$ ./execute_crawl.sh
```
the, images will be saved into same directories above.  
Additionally, the running logs of each queries will be
also saved into `log/yahoo_image_{id of member}.log`.
The Keyakizaka46 members and their IDs are listed in
`member_list.csv`.

## Installation
Installing image_scraper, you type the following command
to the terminal:
```bash
$ cd ~
$ pip install Scrapy
$ git clone https://github.com/Katsuya-Ishiyama/image_scraper.git
```
If you are going to use `execute_crawl.sh` then you
should change its permission like this:
```bash
$ chmod 744 execute_crawl.sh
```

## Directory Structure
```bash
$ tree image_scraper/
image_scraper/
├── LICENSE
├── README.md
├── download
│   └── 001
│       ├── 0001.jpg
│       ├── 0002.jpg
│       └── 0003.jpg
├── execute_crawl.sh
├── image_scraper
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-35.pyc
│   │   ├── items.cpython-35.pyc
│   │   ├── pipelines.cpython-35.pyc
│   │   └── settings.cpython-35.pyc
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-35.pyc
│       │   └── yahoo_image_spider.cpython-35.pyc
│       └── yahoo_image_spider.py
├── member_list.csv
└── scrapy.cfg
```
