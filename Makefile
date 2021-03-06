.PHONY: avoid-too-many-dependencies pip-list
COVERAGE?=0
COVERAGERCFLAG=--rcfile .coveragerc
ifeq ($(COVERAGE), 1)
	PYTHON=coverage run ${COVERAGERCFLAG}
else
	PYTHON=python
endif
PYPI_SERVER?=pypi
GIT_REMOTE_NAME?=origin
SHELL=/bin/bash
VERSION=$(shell python -c"import rosetta_grappelli as m; print(m.__version__)")

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-tox - remove tox artifacts"
	@echo "clean - remove build, python, and tox artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - git tag the current version which creates a new pypi package with travis-ci's help"

clean: clean-build clean-pyc clean-tox

clean-build:
	rm -fr build/
	rm -fr dist/
	find -name *.egg-info -type d | xargs rm -rf

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -type d -exec rm -rf {} +

pip-list:
	pip freeze | tee $@

avoid-too-many-dependencies: pip-list
	test $(shell wc -l pip-list | cut -d' ' -f 1) -le 14

lint:
	flake8 rosetta_grappelli tests --isolated --max-complexity=5

test:
	${PYTHON} manage.py test testapp --traceback
ifeq ($(COVERAGE), 1)
	coverage combine ${COVERAGERCFLAG}
	coverage html ${COVERAGERCFLAG}
	coverage report ${COVERAGERCFLAG} > /dev/null  # fail_under in cfg file
endif

clean-tox:
	if [[ -d .tox ]]; then rm -r .tox; fi

coverage:
	coverage run --source rosetta_grappelli setup.py test
	coverage report -m
	coverage html
	open htmlcov/index.html

docs: outfile=readme-errors
docs:
	rst2html.py README.rst > /dev/null 2> ${outfile}
	cat ${outfile}
	test 0 -eq `cat ${outfile} | wc -l`
	${VERSION}  # can obtain version number - if not, have an explicit error
	grep "^[*] $(shell ${VERSION} | sed "s/-[^.-]\+$$//")\>" README.rst  # ensure we have written the release notes

pre-deploy: clean docs

release: TAG:=v${VERSION}
release: exit_code=$(shell git ls-remote ${GIT_REMOTE_NAME} | grep -q tags/${TAG}; echo $$?)
release:
ifeq ($(exit_code),0)
	@echo "Tag ${TAG} already present"
else
	git tag -a ${TAG} -m"${TAG}"; git push --tags ${GIT_REMOTE_NAME}
endif
