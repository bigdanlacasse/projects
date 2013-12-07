"""

"""
import time
import threading
from storage import WorkQueue
from api_wrapper import GW2

class Manager (object):
    def __init__(self, num_t = 5):
        self.num_threads = num_t
        self.start_time = 0
        self.end_time = 0
        self.exitFlag = 0
        self.threads = []
        self.queueLock = threading.Lock()
        self.work_queue = WorkQueue()
        # Notify threads it's time to exit
        self.exitFlag = 0
    
    def go (self):
        self.start_time = time.time()
        self.fillQueue()
        self.start_threads()
        self.wait()
        self.end_time = time.time()
        
        print 'DONE! Took ' + str(self.end_time - self.start_time) + ' seconds'
    
    """
        Sit around doing nothing whilst the poor, worker threads to ALL THE WORK!
    """
    def wait (self):
        # Wait for queue to empty
        while not self.work_queue.queue.empty():
            print 'Still working... %s items remaining' % str(self.work_queue.queue.qsize())
            time.sleep(5)
        
        print 'QUEUE IS EMPTY!'
        self.exitFlag = 0
        
        # Wait for all threads to complete
        print 'Now waiting for threads to join...'
        for t in self.threads:
            t.join()
        print 'Threads have joined'
            
    """
    
    """    
    def start_threads(self):
        for x in range(0, self.num_threads):
            thread = workerThread(x, self.work_queue.queue, self.queueLock, self.exitFlag);
            thread.start()
            self.threads.append(thread)
        
    """
    
    """
    def fillQueue(self):
        # Fill the queue
        self.queueLock.acquire()
        self.work_queue.fill()
        print 'Initial Queue size: ' + str(self.work_queue.queue.qsize())
        self.queueLock.release()
    

"""

"""
class workerThread (threading.Thread):
    def __init__(self, threadID, q, mutex, exit):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = 'Thread-' + str(self.threadID)
        self.q = q
        self.mutex = mutex
        self.exit = exit
        self.API = GW2()
        
        print self.exit

    def run(self):
        print "Starting " + self.name
        self.process_data()
        print "Exiting " + self.name
        
    def process_data(self):
        while not self.exit:
            self.mutex.acquire()
            if not self.q.empty():
                item = self.q.get()
                self.mutex.release()
                print str(self.name) + ' reporting!'
                print 'Item ID: ' + str(item)
                item_data = self.API.call('item', [item], True)  # Disable debugging
                 
            else:
                self.exit = 1
                self.mutex.release()
            time.sleep(1)