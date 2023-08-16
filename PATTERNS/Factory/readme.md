## Code structure


#### Forecast services
Here I have a simple weather forecast services, each of which can provide its own forecast for different cities.
Services are presented as classes and derived from the single interface *ForecastServiceInterface*. Forecast
services are located in forecast_services.py.

#### Abstract Factory

An interface for creating different factories lies in general_purpose_object_factory.py. It's a simple interface,
whose role is to derive factories client requires. WeatherFactory inherits from abstract factory and located
in AbstractFactory -> weather_factory.py. This file is also a place to register new services.

#### Regular Factory

It's located at Factory -> factory.py. This factory does not need new services to be registered, the process is
automatic – this factory simply scans for any new classes in forecast_services.py with global() function.

# Abstract Factory

What makes this factory abstract, is the fact that factories are themselves derived from some interface. Each
new factory implementation handles (create) some related objects. Interface of that factories designed to
handle almost any kind of objects, that would be created by factories instances, so the interface is pretty
simple and universal.

It basically lets you register any implementation of product, that client would need, stores it and later 
creates its instance. It's not a canonical interface and one can create an instance of that interface as well
(why not?), but the main issue here is the naming – each implementation of a factory should provide methods
with names, related to its job (if application design lets us do that)

So the WeatherFactory, inherited from AbstractFactory, simply renames existing methods:

```python
class WeatherFactory(ObjectFactory):
    ...

    def register_forecast_service(self, service_name: str, service: Type[ForecastServiceInterface]):
        self.register_implementation(service_name, service)
```

That example is pretty far-fetched, I don't think that abstract factories are the best solution, because
factories themselves brings a lot of complexity, and making abstractions from them is too much, IMHO. I would
suggest to create standard factories or even simple factory-methods.

### How it all works

Entrypoint is Script.py, which represents client. Factory created by simply importing variable 'services'
from the file weather_factory.py with concrete factory implementation. It's oversimplified realisation of
factory creation, but it works well and no extra code needed. Registration of products (forecast services)
happens also in weather_factory.py, similarly to what Django does – each line adds new service:

```python
# Register new services here
services = WeatherFactory()
services.register_forecast_service('RANDOM', RandomForecastService)
services.register_forecast_service('GOOD', GoodWeatherOnlyForecastService)
services.register_forecast_service('VENTUSKY', VentuskyForecastNow)
services.register_forecast_service('MARS', MarsForecast)
...
```

After we imported required factory in Script.py, we can ask it to create a service we currently need:

```python
forecast_services = ['VENTUSKY', 'MARS', 'GOOD', 'RANDOM']

for service in forecast_services:
    my_city_weather_service = services.get_weather_service(my_city.city, service)
```

That gives us an instance of weather forcast service, ready to deliver forecast:

```python
print(my_city_weather_service.make_forecast())
```

# Standard Factory

That factory works almost the same, using the same services and almost identical client code. The difference
is that code here a bit lighter, especially on the factory side:

```python
from PATTERNS.Factory.forecast_services import *


class ForcastFactory:
    def create_service(self, service_name: str, city: str):
        if service_name in globals().keys():
            return globals()[service_name](city)
        raise ValueError(service_name)
```

Here our factory simply asks for service name, and that service does not need to be registered somehow. Instead
factory simply searches for service with global() function, which works, because we imported all services from
its file (from PATTERNS.Factory.forecast_services import *).

All the rest is the same – client asks factory to create service instance and works with it.


# Factory Method

Nothing new here, except all the logic from standard factory now lies somewhere on the client side (inside
MyCity class). Method make_forecast_service() makes all the same, that Factory previously did, so the amount
of code is reduced, as well as flexibility.