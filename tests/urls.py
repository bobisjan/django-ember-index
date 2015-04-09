from ember_index.conf.urls import index

from fixtures import Adapter


urlpatterns = [
    index(r'^', 'my-app', Adapter()),
]
