# weather_data_processor.py
import mysql.connector
import requests
from datetime import datetime, timezone, timedelta
import pytz



def fetch_coordinates(suburb):
    db_config = {
    'user': 'remote_user',
    'password': 'Sunnypediag13!',
    'host': '13.237.185.73',
    'port':3306,
    'database': 'Mysql',
    'raise_on_warnings': True,
        }
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        query = "SELECT latitude, longitude FROM postcodes_geo WHERE suburb = %s"
        cursor.execute(query, (suburb,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return result['latitude'], result['longitude']
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    return None, None

    

def fetch_weather_data(suburb, appid):
    lat, lon = fetch_coordinates(suburb)
    if not lat or not lon:
        return None
    url = "https://api.openweathermap.org/data/3.0/onecall"
    params = {
        'lat': lat,
        'lon': lon,
        'exclude': 'minutely,daily',
        'appid': appid,
        'units': 'metric'
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def process_weather_data(data, timezone_location="Australia/Melbourne"):
    melbourne_tz = pytz.timezone(timezone_location)
    processed_data = {
        'today_hourly_uvi': [],
        'tomorrow_hourly_uvi': [],
        'current_alerts': []
    }

    # Current date in Melbourne timezone
    current_dt = datetime.now(tz=melbourne_tz)
    today_date = current_dt.date()
    tomorrow_date = (current_dt + timedelta(days=1)).date()

    for hour in data.get('hourly', []):
        hour_dt = datetime.fromtimestamp(hour['dt'], tz=timezone.utc).astimezone(melbourne_tz)
        if hour_dt.date() == today_date:
            processed_data['today_hourly_uvi'].append({'time': hour_dt.strftime('%Y-%m-%d %H:%M:%S'), 'uvi': hour.get('uvi', '无数据')})
        elif hour_dt.date() == tomorrow_date:
            processed_data['tomorrow_hourly_uvi'].append({'time': hour_dt.strftime('%Y-%m-%d %H:%M:%S'), 'uvi': hour.get('uvi', '无数据')})

    for alert in data.get('alerts', []):
        processed_data['current_alerts'].append({
            'sender_name': alert.get('sender_name'),
            'event': alert.get('event'),
            'start': datetime.fromtimestamp(alert['start'], tz=timezone.utc).astimezone(melbourne_tz).strftime('%Y-%m-%d %H:%M:%S'),
            'end': datetime.fromtimestamp(alert['end'], tz=timezone.utc).astimezone(melbourne_tz).strftime('%Y-%m-%d %H:%M:%S'),
            'description': alert.get('description')
        })

    return processed_data

# # 测试用的API密钥，你应该使用自己的API密钥

# suburb = 'Clayton'
# appid = 'c7f5a3b4b7b713345d680d03698ec31f'
# # Fetch and process weather data
# data = fetch_weather_data(suburb, appid)
# if data:
#     processed_data = process_weather_data(data)
#     print(processed_data)
# else:
#     print("Failed to fetch weather data")
