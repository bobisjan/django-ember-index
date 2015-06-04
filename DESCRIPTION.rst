Django Ember Index
==================

|Build Status| |Code Climate| |Coverage Status| |Requirements Status|

A Django app to serve `Ember`_ index files deployed with
`ember-cli-deploy`_.

Installation
------------

1. Install application using ``$ pip install django-ember-index``.

2. Add ``ember_index`` to your ``INSTALLED_APPS`` setting like this:

  .. code-block:: python

    INSTALLED_APPS = (
        ...
        'ember_index',
    )

Usage
-----

1. Register Ember application(s) at ``urls.py`` with `redis`_\ ’s
   adapter:

  .. code-block:: python

    from ember_index import index, RedisAdapter

    adapter = RedisAdapter(host='localhost')

    urlpatterns = [
        index(r'^other/', 'other-app', adapter),
        index(r'^', 'my-app', adapter),
    ]

  The provided ``regex`` is used to set router’s `rootURL`_ by `replacing`_ pregenerated `baseURL`_ environment configuration at index file.

  Note that `storeConfigInMeta`_ must be set to ``true``, otherwise an exception is raised. If ``base`` tag is present in index file, then value of ``href`` attribute will be replaced too.

  If CSRF protection is enabled, then ``meta`` tag named ``X-CSRFToken`` with generated token will be provided. You can use `Ember Django CSRF`_ to enable protection on the Ember side.

  All adapter’s keyword arguments will be passed into the `StrictRedis`_ object on initialization.

2. Access application(s) at:

  -  ``/`` with current revision of ``my-app``,
  -  ``/r/ed54cda/`` with specific revision of ``my-app``,
  -  ``/other/`` with current revision of ``other-app``,
  -  ``/other/r/ed54cda/`` with specific revision of ``other-app``.

License
-------

Django Ember Index is available under the MIT license. See the LICENSE
file for more info.

.. _Ember: http://emberjs.com
.. _ember-cli-deploy: https://github.com/ember-cli/ember-cli-deploy
.. _redis: http://redis.io
.. _rootURL: http://emberjs.com/api/classes/Ember.Router.html#property_rootURL
.. _replacing: https://github.com/bobisjan/django-ember-index/blob/master/ember_index/utils.py#L1
.. _baseURL: https://github.com/ember-cli/ember-cli/blob/18d377b264859548f41aba6c3ea2015b90978068/blueprints/app/files/config/environment.js#L7
.. _storeConfigInMeta: https://github.com/ember-cli/ember-cli/blob/master/lib/broccoli/ember-app.js#L141
.. _Ember Django CSRF: http://bobisjan.com/ember-django-csrf/
.. _StrictRedis: https://redis-py.readthedocs.org/en/latest/#redis.StrictRedis

.. |Build Status| image:: https://travis-ci.org/bobisjan/django-ember-index.svg?branch=master
   :target: https://travis-ci.org/bobisjan/django-ember-index
.. |Code Climate| image:: https://codeclimate.com/github/bobisjan/django-ember-index/badges/gpa.svg
   :target: https://codeclimate.com/github/bobisjan/django-ember-index
.. |Coverage Status| image:: https://coveralls.io/repos/bobisjan/django-ember-index/badge.svg?branch=master
   :target: https://coveralls.io/r/bobisjan/django-ember-index
.. |Requirements Status| image:: https://requires.io/github/bobisjan/django-ember-index/requirements.svg?branch=master
   :target: https://requires.io/github/bobisjan/django-ember-index/requirements/?branch=master
