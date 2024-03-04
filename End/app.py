from flask import Flask
from flask_restx import Api, Resource,fields
import firebase_admin
from firebase_admin import credentials, db

# 初始化Firebase Admin
cred = credentials.Certificate('./serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://sunnypedia-g13-default-rtdb.firebaseio.com"
})


app = Flask(__name__)
api = Api(app, 
          version='1.0', 
          title='Sample API',
          description='A sample API using Flask-RESTx and Swagger UI')

ns = api.namespace('data', description='Data operations')
# 定义一个资源
@ns.route('/')
class DataList(Resource):
    def get(self):
        """List all data"""
        ref = db.reference('some/path')  # 指定数据库中的路径
        data = ref.get()
        return data

    @api.expect(api.model('DataModel', {
        'name': fields.String(required=True, description='The name'),
        'age': fields.Integer(required=True, description='The age')
    }))
    def post(self):
        """Create a new data entry"""
        ref = db.reference('some/path')  # 指定数据库中的路径
        ref.push(api.payload)
        return {'message': 'Data added successfully.'}, 201

if __name__ == '__main__':
    app.run(debug=True)