import Handlers


class HandlerRegistrator:
    """Registers Handlers in order of their names"""

    def make_handler(self) -> Handlers.AbstractHandler:
        """Searches for all classes with names starting with 'Handler'. Then initiates them one by one. Each Handler
        receives next Handler into attribute ._next.

        Returns:
            first handler in chain, initiated and ready to be used."""

        handlers_list: list[str] = []
        stuff = dir(Handlers)
        for el in stuff:
            if el.startswith('Handler'):
                handlers_list.append(el)

        first_handler = None            # will be returned by this method
        last_initiated_handler = None   # last handler, that was initiated in the loop below

        for i in range(len(handlers_list)):
            handler_name = handlers_list[i]

            if i == len(handlers_list) - 1:
                next_handler_name = None
            else:
                next_handler_name = handlers_list[i+1]

            if not last_initiated_handler:
                handler = getattr(Handlers, handler_name)()
            else:
                handler = last_initiated_handler

            if not first_handler:
                first_handler = handler

            if next_handler_name:
                next_handler = getattr(Handlers, next_handler_name)()
                handler._next = next_handler
                last_initiated_handler = next_handler

        return first_handler
