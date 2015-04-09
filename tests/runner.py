import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TESTS_DIR = os.path.join(BASE_DIR, 'tests')

sys.path.insert(0, TESTS_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')


import django
from django.test.utils import get_runner
from django.conf import settings


def run_tests():
    runner_class = get_runner(settings)
    test_runner = runner_class(pattern='*.py', verbosity=1, interactive=True)
    django.setup()

    failures = test_runner.run_tests(['unit', 'acceptance'])
    sys.exit(bool(failures))


if __name__ == '__main__':
    run_tests()
