from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import View

from ember_index.utils import extend_base_url


class IndexView(View):

    http_method_names = ['get', 'head', 'options']

    manifest = None
    adapter = None

    def get(self, request, revision='current'):
        index_key = self.index_key(revision)
        index = self.adapter.index_for(index_key)

        if not index:
            return self.index_not_found(revision)

        index = self.process_index(index, revision)
        return self.index_response(index)

    def head(self, request, revision='current'):
        response = self.get(request, revision)
        response.content = b''
        return response

    def index_key(self, revision):
        return ':'.join([self.manifest, revision])

    def index_not_found(self, revision):
        content = 'No index found for revision `{1}` of the manifest `{0}`.'
        return HttpResponseNotFound(content.format(self.manifest, revision))

    def index_response(self, index):
        return HttpResponse(index)

    def process_index(self, index, revision):
        return extend_base_url(index, revision)
