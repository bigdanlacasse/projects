from storage import cache

redis_server = cache.setup_redis()

print redis_server.get('item123')
redis_server.set('test', 'bananas!')
print redis_server.get('test')
redis_server.delete('test')
print redis_server.get('test')
