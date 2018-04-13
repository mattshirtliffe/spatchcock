from riak import RiakClient, RiakNode
from flask import Flask, request, jsonify, url_for


app = Flask(__name__)
# client = RiakClient()
# create a bucket
# myBucket = client.bucket('test')

@app.route("/")
def index():
    return jsonify({'message':'All the actions starts at '+ request.url
    + url_for('riak_route')[1:]})

@app.route("/riak", defaults={'key': None}, methods=['GET','POST'])
@app.route("/riak/<key>", methods=['GET'])
def riak_route(key):
    if request.method == 'POST':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return "Hello World!"

# #  {'one':1}
# val1 = 1
# key1 = myBucket.new('one', data=val1)
# key1.store()
#
#
# val2 = "two"
# key2 = myBucket.new('two', data=val2)
# key2.store()
#
#
# val3 = {"myValue": 3}
# key3 = myBucket.new('three', data=val3)
# key3.store()
#
#
# fetched1 = myBucket.get('one')
# fetched2 = myBucket.get('two')
# fetched3 = myBucket.get('three')
#
#
# print(val1 == fetched1.data)
# print(val2 == fetched2.data)
# print(val3 == fetched3.data)
#
#
# fetched3.data['myValue'] = 4
# fetched3.store()
#
# print(fetched3.data)
# fetched3.delete()
# print(fetched3)
#
# print(myBucket.get('three').exists)
