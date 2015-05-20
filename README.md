# Django Ember Index

[![Build Status](https://travis-ci.org/bobisjan/django-ember-index.svg?branch=master)](https://travis-ci.org/bobisjan/django-ember-index) [![Code Climate](https://codeclimate.com/github/bobisjan/django-ember-index/badges/gpa.svg)](https://codeclimate.com/github/bobisjan/django-ember-index) [![Coverage Status](https://coveralls.io/repos/bobisjan/django-ember-index/badge.svg?branch=master)](https://coveralls.io/r/bobisjan/django-ember-index) [![Requirements Status](https://requires.io/github/bobisjan/django-ember-index/requirements.svg?branch=master)](https://requires.io/github/bobisjan/django-ember-index/requirements/?branch=master)

A Django app to serve [Ember](http://emberjs.com) index files deployed with [ember-cli-deploy](https://github.com/ember-cli/ember-cli-deploy).

## Installation

1. Install application using `$ pip install django-ember-index`.

2. Add `ember_index` to your `INSTALLED_APPS` setting like this:

  ```python
  INSTALLED_APPS = (
      ...
      'ember_index',
  )
  ```

## Usage

1. Register Ember application(s) at `urls.py` with [redis](http://redis.io)'s adapter:

  ```python
  from ember_index import index, RedisAdapter

  adapter = RedisAdapter(host='localhost')

  urlpatterns = [
      index(r'^other/', 'other-app', adapter),
      index(r'^', 'my-app', adapter),
  ]
  ```

  _The provided `regex` is used to set router's [rootURL](http://emberjs.com/api/classes/Ember.Router.html#property_rootURL) by [replacing](https://github.com/bobisjan/django-ember-index/blob/master/ember_index/utils.py#L1) pregenerated [baseURL](https://github.com/ember-cli/ember-cli/blob/18d377b264859548f41aba6c3ea2015b90978068/blueprints/app/files/config/environment.js#L7) environment configuration at index file._

  _All adapter's keyword arguments will be passed into the [StrictRedis](https://redis-py.readthedocs.org/en/latest/#redis.StrictRedis) object on initialization._

2. Access application(s) at:

  - `/` with current revision of `my-app`,
  - `/r/ed54cda/` with specific revision of `my-app`,
  - `/other/` with current revision of `other-app`,
  - `/other/r/ed54cda/` with specific revision of `other-app`.


## License

Django Ember Index is available under the MIT license. See the LICENSE file for more info.
