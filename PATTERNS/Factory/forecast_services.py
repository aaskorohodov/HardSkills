import random
import requests
import bs4
from abc import ABC, abstractmethod


class ForecastServiceInterface(ABC):
    @abstractmethod
    def __init__(self, identification):
        self.identification = identification

    @abstractmethod
    def make_forecast(self):
        pass


class RandomForecastService(ForecastServiceInterface):
    def __init__(self, city):
        self.city = city
        self.precipitation = ['rain', 'snow', 'hail']
        self.wind = ['no', 'low', 'high', 'tornado']

    def make_forecast(self):
        forecast = f'RandomForecast (c) – weather for {self.city}:' \
                   f'\n\t– Wind: {random.choice(self.wind)}' \
                   f'\n\t– Precipitations: {random.choice(self.precipitation)}'
        return forecast


class GoodWeatherOnlyForecastService(ForecastServiceInterface):
    def __init__(self, city):
        self.city = city

    def make_forecast(self):
        forecast = f'GoodWeatherOnly (c)– In {self.city} gonna be sunny, warm and nice!'
        return forecast


class VentuskyForecastNow(ForecastServiceInterface):
    def __init__(self, city):
        self.city = city
        self.supported_cities = ['yekaterinburg', 'moscow']

    def make_forecast(self):
        if self.city not in self.supported_cities:
            return 'Ventusky(c) – Wrong city! Can only work with yekaterinburg or moscow!'

        try:
            response = requests.get('https://www.ventusky.com/ru/' + self.city)
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            some_result_set = soup.select(".temperature")
            temperature_now = some_result_set[0].getText().replace(" ", "")
            temperature_now = temperature_now.replace('\n', '')
            temperature_now = temperature_now.replace('\r', '')
            result = f'Ventusky(c) – Temperature in {self.city} is {temperature_now}'
        except Exception as e:
            result = f'Ventusky(c) – Service temporary unavailable. Find programmer or scream for help. Exception:\n{e}'
        return result


class MarsForecast(ForecastServiceInterface):
    def __init__(self, _city):
        self.planet = 'mars'

    def make_forecast(self):
        forecast = 'MarsForecast (c) – temp from -80 to 20 celsius, dust storm, dry, radioactive.'
        return forecast
