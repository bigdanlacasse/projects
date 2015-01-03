"""
    Class which contains storage of queues and threads. Used to start work
"""
import time
import threading
from threads import workerThread
from queing import WorkQueue

class Manager (object):
    def __init__(self, num_t = 5, q_size=50000, missed_only=False):
        self.num_threads = num_t
        self.missed_only = missed_only
        self.start_time = 0
        self.end_time = 0
        self.exitFlag = 0
        self.threads = []
        self.queueLock = threading.Lock()
        self.work_queue = WorkQueue(q_size)
        # Notify threads it's time to exit
        self.exitFlag = 0
    
    """
        Main function to begin working
    """
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
        Start the requested number of threads (of each variety)
    """    
    def start_threads(self):
        for x in range(0, self.num_threads):
            thread = workerThread(x, self.work_queue.queue, self.queueLock, self.exitFlag);
            thread.start()
            self.threads.append(thread)
        
    """
        Call the work queue's fill method to populate the list of items we need to work on
    """
    def fillQueue(self):
        # Fill the queue
        self.queueLock.acquire()
        
        # Determine what data should be used to fill the work queue
        if self.missed_only:
            self.work_queue.fill_from_missing()
        else:
            self.work_queue.fill()
            
        print 'Initial Queue size: ' + str(self.work_queue.queue.qsize())
        self.queueLock.release()