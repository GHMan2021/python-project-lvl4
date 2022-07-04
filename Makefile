install:
	poetry install
lint:
	poetry run flake8 task_manager
start:
	python manage.py runserver
start-gu:
	export DJANGO_SETTINGS_MODULE=task_manager.settings && \
	poetry run gunicorn task_manager.wsgi
makemigrations:
	poetry run python manage.py makemigrations
migrate:
	poetry run python manage.py migrate
test:
	poetry run python manage.py test
shell:
	poetry run python manage.py shell
heroku_migrate:
	heroku run python manage.py migrate
