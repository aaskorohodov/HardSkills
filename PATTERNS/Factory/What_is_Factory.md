Factory Method and Factory Object is a creational design pattern used to create concrete implementations
of a common interface. It separates the process of creating an object from the code that depends on the
interface of the object.

One of the most useful things about factories, is that it lets us use the same code of main application
(aka client) with no need to change and therefor test it, if we make changes to functionality of our 
Factory.

In the example below, if we would try to use the original serializer, then the code would be unchanged 
after we change serializer to Factory. It will still be unchanged if we add more functionality to 
serializer, e.g. create code for serializing into Yaml format.

# Case

```python
import json
import xml.etree.ElementTree as et

class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:
    def serialize(self, song, format):
        if format == 'JSON':
            song_info = {
                'id': song.song_id,
                'title': song.title,
                'artist': song.artist
            }
            return json.dumps(song_info)
        elif format == 'XML':
            song_info = et.Element('song', attrib={'id': song.song_id})
            title = et.SubElement(song_info, 'title')
            title.text = song.title
            artist = et.SubElement(song_info, 'artist')
            artist.text = song.artist
            return et.tostring(song_info, encoding='unicode')
        else:
            raise ValueError(format)
```

```commandline
>>> import serializer_demo as sd
>>> song = sd.Song('1', 'Water of Love', 'Dire Straits')
>>> serializer = sd.SongSerializer()

>>> serializer.serialize(song, 'JSON')
'{"id": "1", "title": "Water of Love", "artist": "Dire Straits"}'

>>> serializer.serialize(song, 'XML')
'<song id="1"><title>Water of Love</title><artist>Dire Straits</artist></song>'

>>> serializer.serialize(song, 'YAML')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "./serializer_demo.py", line 30, in serialize
    raise ValueError(format)
ValueError: YAML
```

The central idea in Factory Method is to provide a separate component with the responsibility to decide
which concrete implementation should be used based on some specified parameter. That parameter in our 
example is the format.

## Implementing factory method

```python
import json
import xml.etree.ElementTree as et


class SongSerializer:
    def serialize(self, song, format):
        serializer = get_serializer(format)
        return serializer(song)


def get_serializer(format):
    if format == 'JSON':
        return _serialize_to_json
    elif format == 'XML':
        return _serialize_to_xml
    else:
        raise ValueError(format)


def _serialize_to_json(song):
    payload = {
        'id': song.song_id,
        'title': song.title,
        'artist': song.artist
    }
    return json.dumps(payload)


def _serialize_to_xml(song):
    song_element = et.Element('song', attrib={'id': song.song_id})
    title = et.SubElement(song_element, 'title')
    title.text = song.title
    artist = et.SubElement(song_element, 'artist')
    artist.text = song.artist
    return et.tostring(song_element, encoding='unicode')
```
*Note that get_serializer() does not execute selected function, but return the function itself (link).

In this implementation:

1. serialize() method is the **client**. It depends on an interface.
2. The interface is a **product**. Concrete implementations are _serialize_to_json() and _serialize_to_xml()
3. _get_serializer() method is the **creator** component


## When to use

#### Replacing complex logical code

**if/elif/else** are hard to maintain, this is a perfect place for factory methods. What you require is 
some kind of parameter (in this example it's a format variable)

#### Constructing related objects from external data

If you need to create a different objects from, lets say, database, you can store type information in that
db as well (type=clerk/sales/manager...).

#### Supporting multiple implementations of the same feature

An image processing application needs to transform a satellite image from one coordinate system  
to another, but there are multiple algorithms with different levels of accuracy to perform the 
transformation.

The application can allow the user to select an option that identifies the concrete algorithm. 
Factory Method can provide the concrete implementation of the algorithm based on this option.

#### Integrating related external services

Situation, when application depends on different APIs. Factory Method may create a concrete service, 
according to client preferences (select API for weather forcast).


## Factory Method as an Object Factory

Object Factory is not just a function, that picks up concrete implementation, but a factory class:

```python
class SerializerFactory:
    def get_serializer(self, format):
        if format == 'JSON':
            return JsonSerializer()
        elif format == 'XML':
            return XmlSerializer()
        else:
            raise ValueError(format)


factory = SerializerFactory()
```

Here get_serializer returns an instance of serializer class:

```python
class JsonSerializer:
    def __init__(self):
        self._current_object = None

    def start_object(self, object_name, object_id):
        self._current_object = {
            'id': object_id
        }

    def add_property(self, name, value):
        self._current_object[name] = value

    def to_str(self):
        return json.dumps(self._current_object)


class XmlSerializer:
    def __init__(self):
        self._element = None

    def start_object(self, object_name, object_id):
        self._element = et.Element(object_name, attrib={'id': object_id})

    def add_property(self, name, value):
        prop = et.SubElement(self._element, name)
        prop.text = value

    def to_str(self):
        return et.tostring(self._element, encoding='unicode')
```

And we can now use it all not with SongSerializer, but with something more generic:

```python
class ObjectSerializer:
    def serialize(self, serializable, format):
        serializer = factory.get_serializer(format)
        serializable.serialize(serializer)
        return serializer.to_str()
```

## No if's

Problem we have now is that SerializerFactory needs to be changed, if new format is added. So, take a look:

```python
class SerializerFactory:

    def __init__(self):
        self._creators = {}

    def register_format(self, format, creator):
        self._creators[format] = creator

    def get_serializer(self, format):
        creator = self._creators.get(format)
        if not creator:
            raise ValueError(format)
        return creator()
```

Now we can add support of the new format by adding new class. In this example we will reuse existing
JsonSerializer to create very similar YamlSerializer, which overwrites single method:

```python
class YamlSerializer(serializers.JsonSerializer):
    def to_str(self):
        return yaml.dump(self._current_object)


serializers.factory.register_format('YAML', YamlSerializer)
```

# General Purpose Object Factory

It's the type of factory, that can be used to create different types of object. Basically it does not
matter which types of object we need – General Purpose Object Factory can create them all.

GPOF does not differ from SerializerFactory, but interfaces it uses does. Here are they are:

```python
class PandoraService:
    def __init__(self, consumer_key, consumer_secret):
        self._key = consumer_key
        self._secret = consumer_secret

    def test_connection(self):
        print(f'Accessing Pandora with {self._key} and {self._secret}')


class PandoraServiceBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, pandora_client_key, pandora_client_secret, **_ignored):
        if not self._instance:
            consumer_key, consumer_secret = self.authorize(
                pandora_client_key, pandora_client_secret)
            self._instance = PandoraService(consumer_key, consumer_secret)
        return self._instance

    def authorize(self, key, secret):
        return 'PANDORA_CONSUMER_KEY', 'PANDORA_CONSUMER_SECRET'


class SpotifyService:
    def __init__(self, access_code):
        self._access_code = access_code

    def test_connection(self):
        print(f'Accessing Spotify with {self._access_code}')


class SpotifyServiceBuilder:
    def __init__(self):
        self._instance = None

    def __call__(self, spotify_client_key, spotify_client_secret, **_ignored):
        if not self._instance:
            access_code = self.authorize(
                spotify_client_key, spotify_client_secret)
            self._instance = SpotifyService(access_code)
        return self._instance

    def authorize(self, key, secret):
        return 'SPOTIFY_ACCESS_CODE'


class LocalService:
    def __init__(self, location):
        self._location = location

    def test_connection(self):
        print(f'Accessing Local music at {self._location}')


def create_local_music_service(local_music_location, **_ignored):
    return LocalService(local_music_location)
```

These are 3 different implementations of interface, that connects either to external music service or to
local collection. Note that the last one is just a function.

Factory itself:

```python
class ObjectFactory:
    def __init__(self):
        self._builders = {}

    def register_builder(self, key, builder):
        self._builders[key] = builder

    def create(self, key, **kwargs):
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)
```

And configs:

```python
config = {
    'spotify_client_key': 'THE_SPOTIFY_CLIENT_KEY',
    'spotify_client_secret': 'THE_SPOTIFY_CLIENT_SECRET',
    'pandora_client_key': 'THE_PANDORA_CLIENT_KEY',
    'pandora_client_secret': 'THE_PANDORA_CLIENT_SECRET',
    'local_music_location': '/usr/data/music'
}

factory = ObjectFactory()
factory.register_implementation('SPOTIFY', SpotifyServiceBuilder())
factory.register_implementation('PANDORA', PandoraServiceBuilder())
factory.register_implementation('LOCAL', create_local_music_service)
```

# Specializing Object Factory to Improve Code Readability

Main drawback of GPOF is that it makes code less readable. To overcome this issue, we can simply derive
new factory from general ObjectFactory, just to make naming better:

```python
class MusicServiceProvider(object_factory.ObjectFactory):
    def get(self, service_id, **kwargs):
        return self.create(service_id, **kwargs)


services = MusicServiceProvider()
services.register_builder('SPOTIFY', SpotifyServiceBuilder())
services.register_builder('PANDORA', PandoraServiceBuilder())
services.register_builder('LOCAL', create_local_music_service)
```

Also, new method get() makes nothing new, it simply invokes method create, but it's name explicitly shows
that create does not actually create new instance each time it's been called. So all we made was simply
changed some names.