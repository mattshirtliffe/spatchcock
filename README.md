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


# Run in Docker
docker build -f Dockerfile -t matthewshirtliffecouk/spatchcock .

docker run -d -p 5000:5000 --net="host" --name spatchcock  matthewshirtliffecouk/spatchcock

# Note
https://www.police.uk/south-yorkshire/KD/crime/+ovSYlx/stats/

Click Download crime data for this area as a CSV file for test data

I also made the keys lowercase
crime_id,month,latitude,longitude,location,category,outcome_status

## Import data
python client.py with crime_data.csv in same dir

# riak libary
https://basho.github.io/riak-python-client/
