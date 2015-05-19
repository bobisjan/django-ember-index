import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'DESCRIPTION.rst')) as description:
    LONG_DESCRIPTION = description.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-ember-index',
    version='0.4.0',
    packages=['ember_index'],
    include_package_data=True,
    test_suite='tests.runner.run_tests',
    license='MIT License',
    description='A Django app to serve Ember index files.',
    long_description=LONG_DESCRIPTION,
    url='http://bobisjan.com/django-ember-index',
    author='Jan Bobisud',
    author_email='me@bobisjan.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.4',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Markup',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
)
