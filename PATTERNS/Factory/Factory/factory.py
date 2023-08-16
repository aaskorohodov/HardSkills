from PATTERNS.Factory.forecast_services import *


class ForcastFactory:
    def create_service(self, service_name: str, city: str):
        if service_name in globals().keys():
            return globals()[service_name](city)
        raise ValueError(service_name)
