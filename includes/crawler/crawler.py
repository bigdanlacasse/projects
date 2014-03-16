"""
  Documentation:    http://wiki.guildwars2.com/wiki/API

  Threading:        http://www.tutorialspoint.com/python/python_multithreading.htm
"""
from utils.manager import Manager

""" 
    Main processing
"""
if __name__ == "__main__":
    # Create manager (a.k.a Task Master) to do the majority of the work
    # @todo: Provide it a list of tasks which need to be done
    num_threads = 15
    max_queue_size = 30000
    
    taskmaster = Manager(num_threads, max_queue_size)
    taskmaster.go() 
    
    
