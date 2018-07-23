# -*- coding: utf-8 -*-

import pathlib
import pandas as pd

member_list = pd.read_csv('member_list.csv')
download_dir = pathlib.Path('./download')

# ---------------------------------------------
# Aggregating number of images at each member
# ---------------------------------------------

member_id = []
member_name = []
image_count = []
for _, (_id, _name) in member_list.iterrows():
    _dir = download_dir / '{:03d}'.format(_id)
    image_path_list = [p for p in _dir.iterdir()]
    member_id.append(_id)
    member_name.append(_name)
    image_count.append(len(image_path_list))

download_image_count = pd.DataFrame(
    data={
        'member_id': member_id,
        'member_name': member_name,
        'image_count': image_count
    }
)
column_order = ['member_id', 'member_name', 'image_count']
download_image_count = download_image_count[column_order]

# ---------------------------------------------
# Display summaries of downloaded images
# ---------------------------------------------

print('Number of downloaded images at each member:')
print(download_image_count)
print()

number_of_members = member_list.shape[0]
print('Number of members: {}'.format(number_of_members))

total_image_count = download_image_count.image_count.sum()
print('Total number of images: {}'.format(total_image_count))

avg_image_count = download_image_count.image_count.mean()
print('Average number of images: {}'.format(avg_image_count))

