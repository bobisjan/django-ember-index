PY := bin/python
PY_VERSION := $(shell ${PY} --version 2>&1 | cut -f 2 -d ' ')

APP := ember_index
COVERAGE := bin/coverage-3.4


coverage:
	${COVERAGE} run --source=${APP} setup.py test
	${COVERAGE} report

test:
	${PY} setup.py test

.PHONY: test
