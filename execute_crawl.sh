#!/bin/sh

csv_file="member_list.csv"

for line in `cat ${csv_file}`
do
    member_id=`echo ${line} | cut -d ',' -f 1`
    member_name=`echo ${line} | cut -d ',' -f 2`
    echo "processing member_id ${member_id}, member_name ${member_name}"
    scrapy crawl yahoo_image -a query=$member_name -a member_id=$member_id --logfile log/yahoo_image_${member_id}.log
done

