from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import View


class IndexView(View):

    http_method_names = ['get', 'head', 'options']

    manifest = None
    adapter = None

    def get(self, request, revision='current'):
        index_key = self.index_key(self.manifest, revision)
        index = self.adapter.index_for(index_key)

        if not index:
            return self.index_not_found(self.manifest, revision)

        index = self.process_index(index)
        return self.index_response(index)

    def head(self, request, revision='current'):
        response = self.get(request, revision)
        response.content = b''
        return response

    def index_key(self, manifest, revision):
        return ':'.join([manifest, revision])

    def index_response(self, index):
        return HttpResponse(index)

    def index_not_found(self, manifest, revision):
        content = 'No index found for revision `{1}` of the manifest `{0}`.'
        return HttpResponseNotFound(content.format(manifest, revision))

    def process_index(self, index):
        return index
