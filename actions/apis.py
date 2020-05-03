import requests

def Weather(city):
	api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0f88f1397cc3e73da5594cc3e5590ec9&q='
	url = api_address + city
	json_data = requests.get(url).json()
	format_add = json_data['main']
	return format_add
