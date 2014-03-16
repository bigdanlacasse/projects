"""
    Worker thread (This guy gets stuff done)
"""
import threading
import time
from api_wrapper import GW2
from storage.db import DB
from utils import dump

class workerThread (threading.Thread):
    def __init__(self, threadID, q, mutex, should_exit):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = 'Thread-' + str(self.threadID)
        self.q = q
        self.mutex = mutex
        self.exit = should_exit
        self.API = GW2()
        self.my_db = DB(collect="items")
        
        print self.exit
    
    """
        Function called by the thread.start
    """
    def run(self):
        print "Starting " + self.name
        self.process_data()
        print "Exiting " + self.name
    
    """
        Where all of the work actually happens. Once called, this will continue pulling items from the queue
        untill all items are completed.
    """
    def process_data(self):
        while not self.exit:
            self.mutex.acquire()
            
            if not self.q.empty():
                item = self.q.get()
                # Once we pop something off the queue, we can release the lock
                self.mutex.release()
                
                # Get the data for this item
                try:
                    item_data = self.API.call('item', [item])  # Disable debugging
                    #dump(item_data, 'Item Dump')
                    
                    # Save this items data
                    self.my_db.insert(item_data)
                except Exception as e:
                    print 'Error: ' + repr(e)
                
            else:
                self.exit = 1
                self.mutex.release()
            time.sleep(1)