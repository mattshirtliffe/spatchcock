from flask import Blueprint, request, jsonify
from marshmallow import schema, ValidationError
from riak import RiakClient

# create crime blueprint
from app.schema import CrimeSchema

crime = Blueprint('crime', __name__)

client = RiakClient()
crime_bucket = client.bucket('crime')

# bucket = client.bucket_type('crime').bucket('category')


@crime.route("/crime", defaults={'crime_id': None}, methods=['GET', 'POST'])
@crime.route("/crime/<crime_id>", methods=['GET','DELETE'])
def crime_route(crime_id):
    if request.method == 'POST':
        # get crime_id and value from request
        # if request.json:

        try:
            crime_schema = CrimeSchema()
            result = crime_schema.load(request.json)
        except ValidationError as err:
            return jsonify({'message': err.messages}), 404

        new_crime = request.json
        new_crime_id = new_crime['crime_id']

        new = crime_bucket.new(new_crime_id, data=new_crime)
        new.store()

        if crime_bucket.get(new_crime_id).exists:
            fetched = crime_bucket.get(new_crime_id)
            return jsonify(fetched.data)

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