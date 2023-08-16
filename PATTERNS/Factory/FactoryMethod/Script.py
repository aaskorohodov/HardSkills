from PATTERNS.Factory.forecast_services import *


class MyCity:
    def __init__(self, city: str):
        self.city = city

    def make_forecast_service(self, service_name):
        if service_name in globals().keys():
            return globals()[service_name](self.city)
        raise ValueError(service_name)


my_city = MyCity('yekaterinburg')
forecast_services = ['RandomForecastService', 'GoodWeatherOnlyForecastService', 'VentuskyForecastNow', 'MarsForecast']

for service in forecast_services:
    my_city_weather_service = my_city.make_forecast_service(service)
    print(my_city_weather_service.make_forecast())
