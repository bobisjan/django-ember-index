class Adapter(object):

    indices = {
        'my-app:ed54cda': '<html><body><h1>ed54cda</h1></body></html>',
        'my-app:d696248': '<html><body><h1>d696248</h1></body></html>',
        'my-app:7fabf72': '<html><body><h1>7fabf72</h1></body></html>',
        'my-app:current': '<html><body><h1>7fabf72</h1></body></html>',
    }

    def index_for(self, key):
        return self.indices.get(key, None)
