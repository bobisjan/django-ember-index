# Django Ember Index

[![Build Status](https://travis-ci.org/bobisjan/django-ember-index.svg?branch=master)](https://travis-ci.org/bobisjan/django-ember-index) [![Coverage Status](https://coveralls.io/repos/bobisjan/django-ember-index/badge.svg)](https://coveralls.io/r/bobisjan/django-ember-index)

A Django app to serve an [Ember](http://emberjs.com) index files deployed with [ember-cli-deploy](https://github.com/ember-cli/ember-cli-deploy).

## Installation

1. Install application using `$ pip install django-ember-index`.

2. Add `ember_index` to your `INSTALLED_APPS` setting like this:

  ```python
  INSTALLED_APPS = (
       ...
       'ember_index',
  )
  ```

3. Register Ember application at `urls.py` with [redis](http://redis.io)'s adapter:

  ```python
  from ember_index.adapters import RedisAdapter
  from ember_index.conf.urls import index

  urlpatterns = [
       index(r'^', 'my-app', RedisAdapter()),
  ]
  ```

  _All keyword arguments will be passed into the [StrictRedis](https://redis-py.readthedocs.org/en/latest/#redis.StrictRedis) object on initialization._

## License

Django Ember Index is available under the MIT license. See the LICENSE file for more info.
