import python_weather
import datetime
import asyncio
import os
from notifypy import Notify

while True:
	async def getweather():
		try:
			async with python_weather.Client(unit=python_weather.METRIC) as client:
				weather = await client.get('Vladivostok')
				message = weather.temperature
				current_time = datetime.datetime.now()
				notification = Notify()
				notification.icon = 'weather/cloudywithsun.png'
				notification.title = "Погода"
				notification.message = f'Температура: {message}°C\nНаправление ветра: {weather.wind_direction}\n{weather.kind}'
				notification.application_name = "pygoda"
				if current_time.strftime("%M:%S") == '11:11':
					notification.send()
				if current_time.strftime("%M:%S") == '41:11':
					notification.send()
		except Exception as e:
			print(e)


	if __name__ == '__main__':
		if os.name == 'nt':
			asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

		asyncio.run(getweather(), debug=True)

input()
