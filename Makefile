install:
	poetry install
lint:
	poetry run flake8 task_manager
start-run:
	python manage.py runserver
start:
	export DJANGO_SETTINGS_MODULE=task_manager.settings && \
	poetry run gunicorn task_manager.wsgi
migrate:
	poetry run python manage.py migrate

