install:
	poetry install
lint:
	poetry run flake8 task_manager
start:
	python manage.py runserver
makemigrations:
	poetry run python manage.py makemigrations
migrate:
	poetry run python manage.py migrate
test:
	poetry run python manage.py test
shell:
	poetry run python manage.py shell

