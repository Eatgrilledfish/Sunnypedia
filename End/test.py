import requests
from datetime import datetime, timezone, timedelta
import pytz
import asyncio
import aiohttp

# 基础信息
lat, lon = -37.930, 145.1275
api_key = 'c7f5a3b4b7b713345d680d03698ec31f'
base_url = 'https://api.openweathermap.org/data/3.0/onecall/timemachine?'
processed_data = {
    'today_hourly_uvi': [],
    'tomorrow_hourly_uvi': [],
    'current_alerts': []
}


# 将原有代码封装成一个方法
async def fetch_uv_index(lat, lon, api_key):
    # 基础信息
    base_url = 'https://api.openweathermap.org/data/3.0/onecall/timemachine?'

    # 当前日期和时区
    tz = pytz.timezone('Australia/Melbourne')
    today = datetime.now(tz).date()
    timestamp = 1710291600 - 3600 - 3600  # 示例中的固定时间戳，实际应用中可能需要动态计算
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

asyncio.run(fetch_uv_index(lat, lon, api_key))

print(processed_data)

        # current_hour = datetime.now(tz).hour
        # if current_hour < 6:
        #     tasks=0
        # elif current_hour > 6:
        #     tasks = [fetch_data(session, hour) for hour in range(6,current_hour)]
        # await asyncio.gather(*tasks)