SHELL := /bin/bash

.PHONY: install
install: env
	source env/bin/activate
	pip install -r requirements.txt
	python manage.py migrate

env:
	virtualenv --python=python3 env
	source env/bin/activate

.PHONY: serve
serve: install
	source env/bin/activate
	python manage.py runserver
