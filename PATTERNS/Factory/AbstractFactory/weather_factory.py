from typing import Type

from PATTERNS.Factory.forecast_services import *
from general_purpose_object_factory import ObjectFactory


class WeatherFactory(ObjectFactory):
    def __init__(self):
        super().__init__()

    def register_forecast_service(self, service_name: str, service: Type[ForecastServiceInterface]):
        self.register_implementation(service_name, service)

    def get_weather_service(self, city, service_name):
        return self.create(service_name, city)


# Register new services here
services = WeatherFactory()
services.register_forecast_service('RANDOM', RandomForecastService)
services.register_forecast_service('GOOD', GoodWeatherOnlyForecastService)
services.register_forecast_service('VENTUSKY', VentuskyForecastNow)
services.register_forecast_service('MARS', MarsForecast)
