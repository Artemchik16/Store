all:
	python manage.py makemigrations
	python manage.py migrate
	isort .
	black .

get-migrate:
	python manage.py makemigrations
	python manage.py migrate

get-code-format:
	isort .
	black .

run:
	python manage.py runserver