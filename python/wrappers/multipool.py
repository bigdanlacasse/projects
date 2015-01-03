"""
    http://api.multipool.us/api.php?api_key=9b290eaadbb270ec40f304e45967c52763749c123a26d94c2c7257592ec36543
"""
import urllib2
import json
from StringIO import StringIO
from utils import dump

class MultipoolAPI(object):
    """ 
        Cgminer RPC API wrapper. 
    """
    def __init__(self, api_key='9b290eaadbb270ec40f304e45967c52763749c123a26d94c2c7257592ec36543'):
        self.data = {}
        self.host = 'http://api.multipool.us/api.php'
        self.url = self.host + '?api_key=' + api_key
    
    """
    
    """
    def fetch(self):
        return self.get_url_contents(self.url, 'JSON')


    """
        Move to base API object
    """
    def get_url_contents(self, url, type='JSON'):
        data = None
        
        # Request the URL and read the response
        responseObj = urllib2.urlopen(url)
        response = responseObj.read()
        
        if type.lower() == 'json': 
            # Use a stream to parse the json into a dict
            json_stream = StringIO(response)
            data = json.load(json_stream)
        else:
            raise Exception('get_url_contants - Type [%s] not implemented' % type)
        
        return data
            

""" 
    Main processing
"""
if __name__ == "__main__":
    multipool = MultipoolAPI()
    return_data = multipool.fetch()
    
    dump(return_data)
            
            
            