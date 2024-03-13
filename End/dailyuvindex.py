# weather_data_processor.py
import mysql.connector
import requests
from datetime import datetime, timezone, timedelta
import pytz
import asyncio
import aiohttp

async def fetch_uv_index(lat, lon, api_key, timestamp,processed_data):
    # 基础信息
    base_url = 'https://api.openweathermap.org/data/3.0/onecall/timemachine?'

    # 当前日期和时区
    tz = pytz.timezone('Australia/Melbourne')
    today = datetime.now(tz).date()
    timestamp = timestamp - 3600   # 示例中的固定时间戳，实际应用中可能需要动态计算
    current_hour = datetime.fromtimestamp(timestamp, tz=timezone.utc).astimezone(tz).strftime('%H')


    async def fetch_data(session, timestamp):
        request_url = f"{base_url}lat={lat}&lon={lon}&dt={timestamp}&appid={api_key}"
        
        # 示例中不会真的发送请求
        async with session.get(request_url) as response:
            data = await response.json()
            uvi = data['data'][0]['uvi']
            time = datetime.fromtimestamp(data['data'][0]['dt'], tz=timezone.utc).astimezone(tz).strftime('%Y-%m-%d %H:%M:%S')
            processed_data['today_hourly_uvi'].append({'time': time, 'uvi': uvi})

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, timestamp - 3600 * (hour - 6)) for hour in range(6, int(current_hour) + 1) if int(current_hour) >= 6]
        await asyncio.gather(*tasks)




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

    

def fetch_weather_data(suburb,lat,lon, appid):

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
        current_dt = response.json()['hourly'][0]['dt']
        return response.json(),current_dt
    else:
        return None

def process_weather_data(data, timezone_location="Australia/Melbourne", current_dt=any):
    melbourne_tz = pytz.timezone(timezone_location)
    processed_data = {
        'today_hourly_uvi': [],
        'tomorrow_hourly_uvi': [],
        'current_alerts': []
    }
    asyncio.run(fetch_uv_index(lat, lon, appid, timestamp = current_dt,processed_data = processed_data))
    # Current date in Melbourne timezone
    current_date = datetime.now(tz=melbourne_tz)
    today_date = current_date.date()
    tomorrow_date = (current_date + timedelta(days=1)).date()

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

suburb = 'Clayton'
appid = 'c7f5a3b4b7b713345d680d03698ec31f'
lat, lon = fetch_coordinates(suburb)
# Fetch and process weather data
data,current_dt = fetch_weather_data(suburb,lat,lon, appid)
if data:
    processed_data = process_weather_data(data,current_dt = current_dt)
    # print(current_dt)
    print(processed_data)
else:
    print("Failed to fetch weather data")
