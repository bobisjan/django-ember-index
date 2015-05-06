from django.conf.urls import include, url
from django.views.generic import RedirectView

from ember_index.views import IndexView


def index(regex, manifest, adapter, path='/', view_class=IndexView):
    view = view_class.as_view(manifest=manifest, adapter=adapter, path=path)
    return url(regex, include([
        url(r'^r/current', RedirectView.as_view(pattern_name=manifest, permanent=False)),
        url(r'^r/(?P<revision>\w+)', view),
        url(r'^', view, name=manifest)
    ]))
