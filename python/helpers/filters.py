"""

"""
from storage import db
from storage import cache
from flask import Markup
from utils import dump

"""
    Build the filters HTML. Implement 'requested_filters' param
"""
def get_browse_filters(requested_filters=None):
    filters = {
               'type' : '',
               'subtype' : ''
               }
    
    filter_data = get_browse_filters_data()
    
    # Primary Filter
    for type in filter_data['types']:
        additional_attrs = ''
        
        if requested_filters is not None and type in requested_filters['item_type']:
            # if this is the selected one, add the selected text
            additional_attrs = 'SELECTED'
            
        filters['type'] += '<option value="%s"%s>%s</option>' % (type, additional_attrs, type)
    filters['type'] = Markup(filters['type'])
    
    # Secondary Filter
    for sup_type in filter_data['subtypes']:
        additional_attrs = 'data-parent="%s"' % filter_data['subtype_mapping'][sup_type]
        
        if requested_filters is not None and sup_type in requested_filters['sub_type']:
            # if this is the selected one, add the selected text
            additional_attrs += ' SELECTED'
            
        filters['subtype'] += '<option value="%s" %s>%s</option>' % (sup_type, additional_attrs, sup_type)
    filters['subtype'] = Markup(filters['subtype'])
    
    return filters
    

"""
 Get the data used to construct the filters. Caching disabled by default for now. 
"""
def get_browse_filters_data(skip_cache=True):
    cached_filters = None
    
    if not skip_cache:
        redis_server = cache.setup_redis()
        cache_key = 'gw2BrowseFilters'
        cached_filters = redis_server.get(cache_key)

    
    # If we don't have the filters in the cache, get them now
    if cached_filters is None:
        cached_filters = {
                            'types' : [],
                            'subtypes' : [],
                            'subtype_mapping' : {}
                          }
        
        # Establish connection
        metaDB = db.DB(collect="meta")
        
        # Figure out the filters
        items_meta = metaDB.find_list()
        
        for item in items_meta:
            cached_filters['types'].append(item['_id'])
            
            # sub_type, count 
            if item['has_subtype']:
                for subtype, count in item['subtypes'].iteritems():
                    cached_filters['subtypes'].append(subtype)
                    cached_filters['subtype_mapping'][subtype] = item['_id']
        
        # Sort the results
        cached_filters['types'].sort()
        cached_filters['subtypes'].sort()
        
        # Cache the results
        if not skip_cache:
            redis_server.set(cache_key, cached_filters)
    
    return cached_filters
    
    
def build_filter_query():
    pass

def store_filters():
    pass