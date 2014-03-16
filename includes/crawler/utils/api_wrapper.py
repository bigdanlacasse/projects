"""

"""
import urllib2
import hashlib
from StringIO import StringIO
import json
from utils import dump

class GW2(object):
    def __init__(self):
        self.urls = {'all_items': 'https://api.guildwars2.com/v1/items.json',
                     'item': 'https://api.guildwars2.com/v1/item_details.json?item_id=',}
    
    """
        Wrapper method for GW API. Call the appropriate method with the provided args.
        Since these are actually just URLs, we just need to know the order of the params
    """
    def call(self, method, args, debug=False):

        url = self.urls[method]
        if len(args):
            url += str(args[0])
        
        # Request the URL and read the response
        response = urllib2.urlopen(url)
        response_json = response.read()
        
        # Hash the raw json, we can use this to determine if objects have changed later
        md5 = hashlib.md5(response_json)
        
        # Use a stream to parse the json into a dict
        json_stream = StringIO(response_json)
        data = json.load(json_stream)
        
        # Store some other relevant bits
        data['url'] = url
        data['hash'] = md5.hexdigest()
        
        # Only get the image for items (not the all items request)
        if method == 'item':
            data['image_url'] = "https://render.guildwars2.com/file/%s/%s.%s" % (data['icon_file_signature'], data['icon_file_id'], 'jpg')
        
        
        # Print some debugging stuff if enabled
        if debug:
            print 'Args: ' + repr(args)
            print 'URL: ' + data['url']
            print 'Data: ' + response_json + '\n-----------------------\n'

        return data