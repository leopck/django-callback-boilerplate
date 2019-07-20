all: 02-build 03-test
	echo "Feel free to run make 04-freeze if the dependencies are what you are looking for"

setup-step-1:
	python3 -m venv env
	echo "Please run this code: source env/bin/activate"

setup-step-2:
	pip install -r requirements.txt


01-start:
	python3 -m venv env
	source env/bin/activate

02-build:
	#Done after every change
	python src/manage.py makemigrations
	python src/manage.py migrate

03-test:
	python src/manage.py runserver 0.0.0.0:9090

04-freeze:
	pip freeze > requirements.txt

05-push:
	../../../tmp/cf/cf push project01 .

99-disable-static:
	##Workaround to fix the static file being call by Django
	../../../tmp/cf/cf set-env project01 DISABLE_COLLECTSTATIC 1

create-sample:
	django-admin startapp quickstart

create-project:
	django-admin startproject project01 src

create-superuser:
	python src/manage.py migrate
	python src/manage.py createsuperuser --email <email> --username admin
