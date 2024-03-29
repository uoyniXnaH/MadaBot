from __future__ import unicode_literals
from pybooru import Danbooru
from random import randint
import requests
import re

def getEroPic() -> str:
    reqTags = 'rating:s -male_focus'
    pages = 100
    client = Danbooru('danbooru')

    randompage = randint(1, pages)
    posts = client.post_list(tags=reqTags, page=randompage, limit=1)
    post = posts[0]
    try:
        picUrl = post['file_url']
    except:
        picUrl = post['source']
        
    picUrl = re.sub('^https', 'http', picUrl, count=1)
	#改为返回图片的url
    # picDat = requests.get(picUrl).content
    
    # picFormat = re.findall('.[a-zA-Z]+$', picUrl)
    # picName = randint(1000, 10000000)
    # picAddr = './plugins/eroPic/{0}'.format(picName)+picFormat[0]
    # with open(picAddr, 'wb') as handle:
        # handle.write(picDat)
    
    return picUrl
