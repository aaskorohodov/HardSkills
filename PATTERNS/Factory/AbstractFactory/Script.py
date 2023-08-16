from weather_factory import services


class MyCity:
    def __init__(self, city: str):
        self.city = city


my_city = MyCity('yekaterinburg')
forecast_services = ['VENTUSKY', 'MARS', 'GOOD', 'RANDOM']

for service in forecast_services:
    my_city_weather_service = services.get_weather_service(my_city.city, service)
    print(my_city_weather_service.make_forecast())
