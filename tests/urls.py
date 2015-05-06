from ember_index.adapters import RedisAdapter
from ember_index.conf.urls import index


adapter = RedisAdapter()

urlpatterns = [
    index(r'^other-app/', 'other-app', adapter),
    index(r'^', 'my-app', adapter),
]
