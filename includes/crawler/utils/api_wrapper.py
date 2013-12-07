"""

"""
import urllib2
import hashlib
from StringIO import StringIO
import json

class GW2(object):
  def __init__(self):
    self.urls = {
      'all_items': 'https://api.guildwars2.com/v1/items.json',
      'item': 'https://api.guildwars2.com/v1/item_details.json?item_id=',
    }

  def call(self, request_type, args, debug=False):
    try:
      url = self.urls[request_type]
      if len(args):
        url += str(args[0])

      response = urllib2.urlopen(url)
      response_json = response.read()
      md5 = hashlib.md5(response_json)
      json_stream = StringIO(response_json)
      data = json.load(json_stream)
      
      if debug:
        print 'URL: ' + url
        print 'HASH: ' + md5.hexdigest()
        print 'Data: ' + response_json + '\n-----------------------\n'
      
      return (data, md5.hexdigest())
    except Exception as e:
      print 'Error: ' + repr(e)