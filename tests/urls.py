from ember_index import index, RedisAdapter


adapter = RedisAdapter()

urlpatterns = [
    index(r'^other/', 'other-app', adapter),
    index(r'^', 'my-app', adapter),
]
