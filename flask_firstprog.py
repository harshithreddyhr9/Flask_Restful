from flask import Flask, jsonify, request

app = Flask(__name__) # __name__ it gives the file a unique name
stores = [
    {
        'name': 'My store',
        'items' : [
            {
                'name': 'Pixel',
                'price': '$816'
            }
        ]
    }
]

@app.route('/') # http.//www/google/com/
def home(): # route is very imp
    return "Welcome to the store"

# POST - used to receive data
# GET - used to send data back only

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name' : request_data['name'],
        'items': []
    }

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if name == store['name']:
            return jsonify(store)
        else :
            return jsonify({'Message': 'store not found'})

@app.route('/store')
def get_stores():
    return jsonify(stores)

@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_in_store(name):
    request_data = request.get_json()
    
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

app.run(port=5000, debug=True)  