from django.conf.urls import include, url
from django.views.generic import RedirectView

from ember_index.views import IndexView


def index(regex, manifest, adapter, view_class=IndexView):
    '''Create URL pattern for Ember application.

    Ember application will be accessible at these paths (prefixed with `regex`):

        1. `/` ,
        2. `/r/:revision/`,
        3. `/r/current/`, which redirects to `/`.

    Keyword arguments:
        regex (string): A regex from Ember application is served.
        manifest (string): A name of Ember application.
        adapter (object): An adapter for index provider.
        view_class (ember_index.views.IndexView): An index view (default IndexView).

    Returns:
        An URL pattern for Ember application.

    '''
    view = view_class.as_view(manifest=manifest, adapter=adapter, regex=regex)
    redirect = RedirectView.as_view(pattern_name=manifest, permanent=False)

    return url(regex, include([
        url(r'^r/current', redirect),
        url(r'^r/(?P<revision>\w+)', view),
        url(r'^', view, name=manifest)
    ]))
