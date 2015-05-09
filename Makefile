PY := bin/python
PY_VERSION := $(shell ${PY} --version 2>&1 | cut -f 2 -d ' ')

COVERAGE_VERSION := $(shell echo '${PY_VERSION}' | grep -po '\d.\d')
COVERAGE := bin/coverage-${COVERAGE_VERSION}

APP := ember_index

coverage:
	${COVERAGE} run --source=${APP} setup.py test
	${COVERAGE} report

test:
	${PY} setup.py test

.PHONY: test
