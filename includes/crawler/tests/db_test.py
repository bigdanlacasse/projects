from storage.db import DB
from utils import dump


# Instantiate Object
my_db = DB(collect="items")

"""
Drop collection
"""
#dump(my_db.drop_collection())

"""
Insert a new record
"""
#my_db.insert({'item' : 5515, 'type' : 'weapon'})

"""
Find one record
"""
qry = {'type' : 'weapon'}
test = my_db.findOne()
dump(test)

"""
Find all record (returns cursor)
"""
#test2 = my_db.find_list()
#dump(test2)

"""
Find all record (returns list)
"""
#test2 = my_db.find_list()
#dump(test2)



