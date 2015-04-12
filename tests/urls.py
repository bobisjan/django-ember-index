from ember_index.adapters import RedisAdapter
from ember_index.conf.urls import index


urlpatterns = [
    index(r'^', 'my-app', RedisAdapter()),
]
