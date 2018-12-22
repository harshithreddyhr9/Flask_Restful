from flask import Flask,jsonify
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

items=["hi", 2,3]
class Item(Resource):
    def get(self):
        return jsonify(items)
        

class Items(Resource):
    def post(self,name):
        item = {'name':name, 'price':12.00}
        items.append(item)
        return item, 201
    def delete(self,name):
        items.remove(name)
        return 202
api.add_resource(Items, '/item/<string:name>')
api.add_resource(Item, '/items')
app.run(port=5000, debug=True)