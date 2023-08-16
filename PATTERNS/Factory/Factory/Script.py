from factory import ForcastFactory


class MyCity:
    def __init__(self, city: str):
        self.city = city


my_city = MyCity('yekaterinburg')
forecast_services = ['RandomForecastService', 'GoodWeatherOnlyForecastService', 'VentuskyForecastNow', 'MarsForecast']

for service in forecast_services:
    my_city_weather_service = ForcastFactory().create_service(service, my_city.city)
    print(my_city_weather_service.make_forecast())
