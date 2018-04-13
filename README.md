# Run

pipenv --python 3.6
pipenv shell

pipenv install flask
pipenv install riak

export FLASK_APP=main.py
flask run
