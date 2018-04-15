# API for South Yorkshire Crime Data

# Run

pipenv --python 3.6

pipenv shell

pipenv install flask

pipenv install marshmallow

pipenv install riak

export FLASK_APP=run.py

export FLASK_DEBUG=1

flask run


# Note
https://www.police.uk/south-yorkshire/KD/crime/+ovSYlx/stats/

Click Download crime data for this area as a CSV file for test data

I also made the keys lowercase
crime_id,month,latitude,longitude,location,category,outcome_status

# riak libary
https://basho.github.io/riak-python-client/



