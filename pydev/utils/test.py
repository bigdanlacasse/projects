"""
  Documentation:    http://wiki.guildwars2.com/wiki/API

  Threading:        http://www.tutorialspoint.com/python/python_multithreading.htm
"""
import urllib2
import hashlib
from StringIO import StringIO
import json
import time
import threading
import Queue


num_threads = 5
start_time = time.time()

"""
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
  if (count > 1):
    break

print 'DONE! Took ' + str(time.time() - start_time) + ' seconds'
"""

class gw2API(object):
  def __init__(self):
    self.urls = {
      'all_items': 'https://api.guildwars2.com/v1/items.json',
    }

  def call(self, request_type, args):
    try:
      url = self.urls[request_type]
      if len(args):
        url = url % args

      response = urllib2.urlopen(url)
      response_json = response.read()
      json_stream = StringIO(response_json)
      data = json.load(json_stream)

      return data
    except Exception as e:
      print e


class gwItemsQueue(object):
  def __init__(self):
    self.queue = Queue.Queue(1000)
    self.API = gw2API()

  def fill(self):
    all_items = self.API.call('all_items', [])
    for item in all_items['items']:
      try:
        self.queue.put(item, False)
      except Exception as e:
        print 'Queue is full, sorry!'
        break

class myThread (threading.Thread):
    def __init__(self, threadID, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = 'Thread-' + str(self.threadID)
        self.q = q

    def run(self):
        print "Starting " + self.name
        process_data(self.name, self.q)
        print "Exiting " + self.name

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not q.empty():
            data = q.get()
            queueLock.release()
            print "%s processing %s" % (threadName, data)
        else:
            queueLock.release()
        time.sleep(1)




exitFlag = 0
threads = []
queueLock = threading.Lock()
workQueue = gwItemsQueue()

for x in range(1, num_threads):
  thread = myThread(x, workQueue.queue);
  thread.start()
  threads.append(thread)

# Fill the queue
queueLock.acquire()
workQueue.fill()
queueLock.release()

# Wait for queue to empty
while not workQueue.queue.empty():
    pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()
print "Exiting Main Thread"



"""
workQueue.fill()
print 'Done'
print workQueue.queue.qsize()
"""