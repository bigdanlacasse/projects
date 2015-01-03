"""
  Documentation:    http://wiki.guildwars2.com/wiki/API

  Threading:        http://www.tutorialspoint.com/python/python_multithreading.htm
"""
import urllib2
import hashlib
from StringIO import StringIO
import json
import time

start_time = time.time()

data = urllib2.urlopen('https://api.guildwars2.com/v1/items.json')
items_json = data.read()
io = StringIO(items_json)
items = json.load(io)

print len(items['items'])

count = 0
for item in items['items']:
  count+=1
  print 'Item ID: ' + str(item)
  detail_url = 'https://api.guildwars2.com/v1/item_details.json?item_id=' + str(item)
  detail_data = urllib2.urlopen(detail_url)
  details_json = detail_data.read()
  md5 = hashlib.md5(details_json)
  print 'URL: ' + detail_url
  print 'HASH: ' + md5.hexdigest()
  print details_json + '\n-----------------------\n'
  if (count > 100):
    break

print 'DONE! Took ' + str(time.time() - start_time) + ' seconds'