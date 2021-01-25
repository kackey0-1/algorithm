## DRF [Django Rest Framework]
[Sample Code](https://github.com/akiyoko/drf-simplest-sample)

### First Step
```bash
# Run Application
python manage.py runserver
# Make Migragtion
python manage.py makemigrations
# Exec Migration 
python manage.py migrate
# Interactive Shell
python manage.py shell
# Create Super User
python manage.py createsuperuser
```

### Setup React
```bash
# ref: https://www.valentinog.com/blog/drf/
# create frontend
django-admin startapp frontend
# create componets folder
mkdir -p ./frontend/src/components
# create componets static, templates
mkdir -p ./frontend/{static,templates}/frontend
# initialize environment
cd ./frontend && npm init -y
# nstall webpack and webpack cli
npm i webpack webpack-cli --save-dev
# install babel for transpiling our code
npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
# pull in React
npm i react react-dom --save-dev

```