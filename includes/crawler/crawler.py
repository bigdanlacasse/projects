"""
  Documentation:    http://wiki.guildwars2.com/wiki/API

  Threading:        http://www.tutorialspoint.com/python/python_multithreading.htm
"""
from utils.manager import Manager

""" 
    Main processing
"""
if __name__ == "__main__":
    # @todo: check database connectivity    
    # Create manager (a.k.a Task Master) to do the majority of the work
    # @todo: Provide it a list of tasks which need to be done
    taskmaster = Manager(100)
    taskmaster.go() 
    
    
