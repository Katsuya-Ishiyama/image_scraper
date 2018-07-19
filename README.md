# image_scraper
## Overview
image_scraper, based on scrapy, has been designed to download images of
Keyakizaka46.  
Yahoo Japan is used for the search engine.

## Usage
If you would like to get the images of 1 member, you are
able to execute the following code.
```bash
$ scrapy crawl yahoo_image -a query={your query} -a member_id={id of member}
```

