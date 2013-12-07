import Queue
from api_wrapper import GW2

class WorkQueue(object):
  def __init__(self, size=10000):
    self.queue = Queue.Queue(size)
    self.API = GW2()

  def fill(self):
    reponse = self.API.call('all_items', [])
    for item in reponse[0]['items']:
      try:
        self.queue.put(item, False)
      except Exception as e:
        print 'Queue is full, sorry!'
        break
