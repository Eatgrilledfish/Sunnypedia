from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS

app = Flask(__name__)
# 允许来自任何来源的跨域请求到 /api/ 路径。
CORS(app, resources={r"/*": {"origins": "*"}})
app.config["SECRET_KEY"] = "12345678"

api = Api(app, version='1.0', title='Sample API',
          description='A sample API')


ns = api.namespace('hello', description='Hello operations')

# model
hello_model = api.model('HelloModel', {
    'message': fields.String(required=True, description='A hello message')
})

@ns.route('/')  # rounter
class HelloWorld(Resource):
    @ns.doc('get_hello')  # Document description
    @ns.marshal_with(hello_model)  # output
    def get(self):
        '''Fetch a greeting'''
        return {'message': 'Hello, World!'}

if __name__ == '__main__':
    app.run(debug=True)
