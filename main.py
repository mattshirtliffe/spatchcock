from riak import RiakClient, RiakNode
from flask import Flask, request, jsonify, url_for

app = Flask(__name__)
client = RiakClient()

# create and get bucket
bucket = client.bucket('test')

@app.route("/")
def index():
    return jsonify({'message': 'All the actions starts at ' + request.url
                               + url_for('riak_route')[1:]})


@app.route("/riak", defaults={'key': None}, methods=['GET', 'POST'])
@app.route("/riak/<key>", methods=['GET','DELETE'])
def riak_route(key):
    if request.method == 'POST':

        # get key and value from request
        # if request.json:
        new_key = request.json['key']
        data = request.json['data']

        # check both key and data are set - truthy
        if new_key and data:
            new = bucket.new(new_key, data=data)
            new.store()
            if bucket.get(new_key).exists:
                fetched = bucket.get(new_key)
                return jsonify(fetched.data)
        else:
            return jsonify({'message':'missing key or data'}), 404

    elif request.method == 'DELETE':

        if bucket.get(key).exists:
            fetched = bucket.get(key)
            fetched.delete()
            return jsonify({'message':'deleted'})
        else:
            return jsonify({'message': key + ' not found'}), 404
    else:
        if not key:
            return jsonify({'message': 'give me a key I am hungry '+request.url
                               +'/<key>'}), 404
        else:
            if bucket.get(key).exists:
                fetched = bucket.get(key)
                return jsonify(fetched.data)
            else:
                return jsonify({'message': key + ' not found'}), 404