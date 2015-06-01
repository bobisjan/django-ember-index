from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import View

from ember_index.utils import path_for, replace_base_url


class IndexView(View):
    '''A class based view for serving index files of Ember applications.

    Every application has a `current` index file and one or many revisioned index files.

    These index files are accessible by `GET` request on this view.

    Attributes:
        http_method_names (list): A list of supported HTTP methods.
        manifest (string): A name of Ember application.
        adapter (object): An adapter for index provider.
        regex (string): A regex from Ember application is served.
        request: (django.http.HttpRequest): An instance of the current request.

    '''

    http_method_names = ['get', 'head', 'options']

    manifest = None
    adapter = None
    regex = None

    request = None

    def get(self, request, revision='current'):
        '''Handle `GET` request for index of Ember application.

        Keyword arguments:
            request (django.http.HttpRequest): An instance of HTTP request.
            revision (string): A requested revision, which defaults to `current`.

        Returns:
            An instance of `django.http.HttpResponse` with index as it's content.

            If no index is found then an instance of `django.http.HttpResponseNotFound` is returned.

        '''
        self.request = request

        index_key = self.index_key(revision)
        index = self.adapter.index_for(index_key)

        if not index:
            return self.index_not_found(revision)

        index = self.process_index(index, revision)
        return self.index_response(index)

    def head(self, request, revision='current'):
        '''Handle `HEAD` request for index of Ember application.

        Keyword arguments:
            request (django.http.HttpRequest): An instance of HTTP request.
            revision (string): A requested revision, which defaults to `current`.

        Returns:
            A same response like `GET` method, but without any content.

        '''
        response = self.get(request, revision)
        response.content = b''
        return response

    def index_key(self, revision):
        '''Join manifest and revision with `:` to build an index key.

        Keyword arguments:
            revision (string): A requested revision.

        Returns:
            A key used to index lookup.

        '''
        return ':'.join([self.manifest, revision])

    def index_not_found(self, revision):
        '''Return `django.http.HttpResponseNotFound`.

        Keyword arguments:
            revision (string): A requested revision.

        Returns:
            An instance of `django.http.HttpResponseNotFound` class.

        '''
        content = 'No index found for revision `{1}` of the manifest `{0}`.'
        return HttpResponseNotFound(content.format(self.manifest, revision))

    def index_response(self, index):
        '''Return index within `django.http.HttpResponse`.

        Keyword arguments:
            index (string): An index for requested revision.

        Returns:
            An instance of `django.http.HttpResponse` class with index as it's content.

        '''
        return HttpResponse(index)

    def process_index(self, index, revision):
        '''A hook which allows to modify an index.

        By default it replaces `baseURL` in environment configuration.

        If CSRF protection is enabled, then `meta` tag with CSRF token will be provided.

        Keyword arguments:
            index (string): An index for requested revision.
            revision (string): A requested revision.

        Returns:
            A processed index.

        '''
        index = replace_base_url(index, revision, self.path)

        if self.is_csrf_protection_enabled:
            index = self.append_meta_with_csrf_token(index)

        return index

    @property
    def path(self):
        return path_for(self.regex)

    @property
    def is_csrf_protection_enabled(self):
        return 'django.middleware.csrf.CsrfViewMiddleware' in settings.MIDDLEWARE_CLASSES

    @property
    def csrf_meta_name(self):
        return 'X-CSRFToken'  # HTTP_X_CSRFTOKEN

    def append_meta_with_csrf_token(self, index):
        '''Return index with CSRF token in meta tag named `X-CSRFToken`.

        Keyword arguments:
            index (string): An index for requested revision.

        Returns:
            An index with CSRF token.

        '''
        from django.middleware.csrf import get_token

        start = index.index('</head>')
        meta = '<meta name="{0}" content="{1}">'
        meta = meta.format(self.csrf_meta_name, get_token(self.request))

        return index[:start] + meta + index[start:]
