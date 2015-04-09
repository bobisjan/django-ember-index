from django.conf.urls import include, url

from ember_index.views import IndexView


def index(regex, manifest, adapter, view_class=IndexView):
    view = view_class.as_view(manifest=manifest, adapter=adapter)
    return url(regex, include([
        url(r'^r/(?P<revision>\w+)', view),
        url(r'^', view)
    ]))
