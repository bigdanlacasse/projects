"""
  Documentation:    http://wiki.guildwars2.com/wiki/API

  Threading:        http://www.tutorialspoint.com/python/python_multithreading.htm
"""
from utils.manager import Manager
from helpers.data_mapping import MetaData

""" 
    Main processing
"""
if __name__ == "__main__":
    # Create manager (a.k.a Task Master) to do the majority of the work
    # @todo: Provide it a list of tasks which need to be done
    num_threads = 15 # 15
    max_queue_size = 50000 # 30,000
    missed_only = False
    
    print('Running main crawler....')
    taskmaster = Manager(num_threads, max_queue_size, missed_only)
    taskmaster.go() 
    
    print('Populating Meta Data.....')
    md = MetaData()
    md.populate()
    print('Done')
    
