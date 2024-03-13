from flask import Flask,request
from flask_restx import Api, Resource,fields
from flask_cors import CORS
from calculate_sunscreen import calculate_sunscreen_amount
from UvindexApi import process_weather_data, fetch_weather_data, fetch_coordinates
import mysql.connector



app = Flask(__name__)
CORS(app)

api = Api(app, 
          version='1.0', 
          title='Sample API',
          description='A sample API using Flask-RESTx and Swagger UI')

ns = api.namespace('data', description='Data operations')

db_config = {
    'user': 'remote_user',
    'password': 'Sunnypediag13!',
    'host': '13.237.185.73',
    'port': 3306,
    'database': 'Mysql',
    'raise_on_warnings': True,
}


# define a data model
sunscreen_model = api.model('SunscreenCalculation', {
    'gender': fields.String(required=True, description='Gender of the user', enum=['male', 'female']),
    'height': fields.Float(required=True, description='Height of the user in centimeters'),
    'weight': fields.Float(required=True, description='Weight of the user in kilograms'),
    'head': fields.String(description='Headwear option selected by the user'),
    'top': fields.String(description='Topwear option selected by the user'),
    'bottom': fields.String(description='Bottomwear option selected by the user'),
    'shoes': fields.String(description='Shoes option selected by the user'),
})

weather_model = api.model('WeatherData', {
    'suburb': fields.String(required=True, description='Suburb name for weather data fetching'),
})


@ns.route('/sunscreen')
class SunscreenCalculation(Resource):
    @api.expect(sunscreen_model)
    def post(self):
        # Extract the data from the request
        data = api.payload
        gender = data['gender']
        height = data['height']
        weight = data['weight']
        head = data.get('head', '')
        top = data.get('top', '')
        bottom = data.get('bottom', '')
        shoes = data.get('shoes', '')
        
        # Perform the calculation
        result = calculate_sunscreen_amount(gender, height, weight, head, top, bottom, shoes)
        
        # Return the result
        return result

@ns.route('/weather')
class WeatherData(Resource):
    @api.expect(weather_model)
    def post(self):
        # 提取请求中的数据
        data = api.payload
        suburb = data['suburb']
        appid = '55692ade591c39c9d006377c0702e77f'
        # Fetch and process weather data
        lat, lon = fetch_coordinates(suburb)
        data,current_dt = fetch_weather_data(suburb, lat,lon, appid)
        if data:
            processed_data = process_weather_data(data,current_dt = current_dt,lat=lat,lon=lon, appid=appid)
            return processed_data
        else:
            return "Failed to fetch weather data"
        
@ns.route('/suburbs')
class Suburbs(Resource):
    def get(self):
        """Return a list of all suburbs from the database"""
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute("SELECT DISTINCT suburb FROM postcodes_geo")
            suburbs = cursor.fetchall()
            cursor.close()
            conn.close()
            return [suburb[0] for suburb in suburbs]
        except Exception as e:
            api.abort(500, str(e))


        
@ns.route('/graph')
class Suburbs(Resource):
    def get(self):
        """Return a list of all suburbs from the database"""
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            cursor.execute("SELECT Year, mortality_rate_per_100000, incidence_rate_per_100000 FROM mortality_and_incidence")
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            years = []
            mortality_rates = []
            incidence_rates = []
            for row in rows:
                years.append(row[0])
                mortality_rates.append(row[1])
                incidence_rates.append(row[2])
            data = {
                "years": years,
                "mortality_rates_per_100000": mortality_rates,
                "incidence_rates_per_100000": incidence_rates
            }
            return data
        except Exception as e:
            api.abort(500, str(e))



if __name__ == '__main__':
    app.run(debug=True)