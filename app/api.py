from flask import Flask
from flask_restful import Resource, Api
from getGenders import getGenders

app = Flask(__name__)
api = Api(app)

test = '{"gender1": "action", "gender2": "terror", "gender3": "comedy"}'

class setGenero(Resource):
    def get(self, genero):
        return genero

class Test(Resource):
    def get(self):
        genders = getGenders(test)
        return genders

api.add_resource(Test, '/')
api.add_resource(setGenero, '/setGenero/<string:genero>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
