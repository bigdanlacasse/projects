"""
    Based on built-in queue. All we've really added here is a fill method
    and the concept of a maximum queue size (respected only when the fill method is used)
"""
import Queue
from api_wrapper import GW2

class WorkQueue(object):
    def __init__(self, size=50000):
        self.queue = Queue.Queue(size)
        self.API = GW2()
    
    """
        Populate the queue with all the items
    """
    def fill(self):
        reponse = self.API.call('all_items', [])
        for item in reponse['items']:
            try:
                self.queue.put(item, False)
            except Exception as e:
                print 'Queue is full, sorry! -- ' + e.message
                break
