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


