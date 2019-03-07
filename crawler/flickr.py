# pip install flickrapi
import flickrapi
import urllib.request
import os
from collections import OrderedDict
from datetime import datetime

flickr=flickrapi.FlickrAPI('c6a2c45591d4973ff525042472446ca2', '202ffe6f387ce29b', cache=True)

# license dict
license = {
    "cc-by-nc-sa": {
        "id": 1, "name": "Attribution-NonCommercial-ShareAlike License (CC BY-NC-SA)",
        "url": "https://creativecommons.org/licenses/by-nc-sa/2.0/"},
    "cc-by-nc": {
        "id": 2, "name": "Attribution-NonCommercial License (CC BY-NC)",
        "url": "https://creativecommons.org/licenses/by-nc/2.0/"},
    "cc-by": {
        "id": 4, "name": "Attribution License (CC BY)",
        "url": "https://creativecommons.org/licenses/by/2.0/"},
    "cc-by-sa": {
        "id": 5, "name": "Attribution-ShareAlike License (CC BY-SA)",
        "url": "https://creativecommons.org/licenses/by-sa/2.0/"},
    "cc0": {
        "id": 9, "name": "Public Domain Dedication (CC0)",
        "url": "https://creativecommons.org/publicdomain/zero/1.0/"},
    "public": {
        "id": 10, "name": "Public Domain Mark",
        "url": "https://creativecommons.org/publicdomain/mark/1.0/"}}

# For information about arguments, see https://www.flickr.com/services/api/flickr.photos.search.html
min_upload_date='2011-1-1'
max_upload_date='2018-12-31'
url_type='k'                # (1) 수정포인트: 고화질 -> 범위 확장 필요함
keyword = 'tiger'
max_title_len = 15
license_type = 'cc-by-sa'
license_id = license[license_type]['id']
license_name = license[license_type]['name']
license_url = license[license_type]['url']
print('License name: {}'.format(license_name))
print('License url: {}'.format(license_url))

photo_loader = flickr.walk(
    text=keyword,
    #tags=tag,
    #tag_mode='all',
    extras='description, owner_name, date_upload, url_{}'.format(url_type),
    sort='relevance',
    content_type=1,     # photos only
    min_upload_date=min_upload_date,
    max_upload_date=max_upload_date,
    license=license_id,
    pages=100,
    per_page=500,      # 500 is maximum
    safe_search=1)

photos = OrderedDict()
photo_idx = 0
# crawl photo urls and metadata
for i, photo in enumerate(photo_loader):
    url = photo.get('url_{}'.format(url_type))
    title = photo.get('title').lower()
    if (url is not None) and len(title) < max_title_len:
        photos[photo_idx] = OrderedDict()

        # metadata
        photos[photo_idx]['photo_url'] = url
        photos[photo_idx]['photo_title'] = photo.get('title')
        photos[photo_idx]['author'] = photo.get('ownername')

        time_stamp = int(photo.get('dateupload'))
        date = datetime.utcfromtimestamp(time_stamp).strftime('%Y-%m-%d')
        photos[photo_idx]['date_uploaded'] = date

        # pixel size
        height = int(photo.get('height_{}'.format(url_type)))
        width = int(photo.get('width_{}'.format(url_type)))
        photos[photo_idx]['pixel_size'] = [height, width]

        # license info
        photos[photo_idx]['license'] = license_name
        photos[photo_idx]['license_url'] = license_url

        photo_idx += 1

    if (i + 1) % 100 == 0:
        print('Iterations: {}, Number of photos: {}'.format(i + 1, photo_idx))  # enumerate에 의해서

    # comment out the below lines for real usage
    if (i + 1) > 1000:
        break

idx = 0
print(photos[idx])
# print(photos[idx]['photo_url'])