from flask import Blueprint, request, jsonify
from riak import RiakClient

# create crime blueprint
crime = Blueprint('crime', __name__)

client = RiakClient()
crime_bucket = client.bucket('crime')

@crime.route("/crime", defaults={'crime_id': None}, methods=['GET', 'POST'])
@crime.route("/crime/<crime_id>", methods=['GET','DELETE'])
def crime_route(crime_id):
    if request.method == 'POST':
        # get crime_id and value from request
        # if request.json:
        new_crime = request.json
        new_crime_id = new_crime['crime_id']

        # check both crime_id and data are set - truthy
        if new_crime_id:
            new = crime_bucket.new(new_crime_id, data=new_crime)
            new.store()

            if crime_bucket.get(new_crime_id).exists:
                fetched = crime_bucket.get(new_crime_id)
                return jsonify(fetched.data)


        else:
            return jsonify({'message': 'missing crime_id'}), 404

    elif request.method == 'DELETE':

        if crime_bucket.get(crime_id).exists:
            fetched = crime_bucket.get(crime_id)
            fetched.delete()
            return jsonify({'message': 'deleted'})
        else:
            return jsonify({'message': crime_id + ' not found'}), 404
    else:
        if not crime_id:
            keys = crime_bucket.get_keys()
            keys = keys[0:10]
            return jsonify({'crimes': keys})
        else:
            if crime_bucket.get(crime_id).exists:
                fetched = crime_bucket.get(crime_id)
                return jsonify(fetched.data)
            else:
                return jsonify({'message': crime_id + ' not found'}), 404


@crime.route("/test", methods=['GET', 'POST'])
def test():
    print(request.json)
    return jsonify(request.json), 200