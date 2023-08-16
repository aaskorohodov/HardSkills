class ObjectFactory:
    """General Purpose Object Factory. Can be used with any types of objects, but for better code readability it is
    recommended to inherit new Factory, so that naming was more obvious"""

    def __init__(self):
        """self._implementation stores registered implementation (interfaces implementations)"""

        self._implementation = {}

    def register_implementation(self, key: str, builder: any):
        """Registers implementation (interfaces implementations)"""

        self._implementation[key] = builder

    def create(self, key: str, *args):
        """Finds and invokes builders. If kwargs provided – calls builder with that kwargs."""

        implementation = self._implementation.get(key)
        if not implementation:
            raise ValueError(key)
        return implementation(*args)
