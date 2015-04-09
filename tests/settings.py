INSTALLED_APPS = (
    'ember_index',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'testdb',
    }
}

ROOT_URLCONF = 'urls'

SECRET_KEY = 'a1b2c3d4'
