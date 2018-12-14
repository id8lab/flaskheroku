Setup your account on heroku
Setup your account on mlab.com

heroku apps:create unique-name-of-your-app

create python env:
python -m venv venv

pip install gunicorn

save dependency packages
pip freeze > requirements.txt


test local
$ export FLASK_APP=main.py
$ flask run

Flask environment set as .flaskenv

Procfile contain the launch of the python application.

## MongoDB access
To access MongoDB I have created a mongodb on mlab.com




