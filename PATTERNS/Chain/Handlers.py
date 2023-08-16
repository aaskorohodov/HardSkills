from abc import ABC, abstractmethod
from typing import Optional
import re


class AbstractHandler(ABC):
    """Interface for the chain of Handlers"""

    def __init__(self):
        """self._next stores next Handler, if there is one"""

        self._next = None

    def handle(self, request: str) -> str:
        """Method, to be called, for initiating chain of Handlers"""

        handled = self.process_request(request)

        if not handled:
            if self._next:
                return self._next.handle(request)
            else:
                return 'All handlers failed'
        else:
            return handled

    @abstractmethod
    def process_request(self, request: str) -> Optional[str]:
        """Logic of specific handler"""
        pass


class Handler1DataChecker(AbstractHandler):
    """Checks incoming data for unsupported operators and explicitly wrong expression"""

    def process_request(self, request):
        allowed_symbols = list('1234567890/*-+')
        operators = ['/', '*', '-', '+']

        for symbol in request:
            if symbol not in allowed_symbols:
                return f'Symbol "{symbol}" is not allowed! But it is in your expression.'

        for operator in operators:
            if request.startswith(operator):
                return f'Your expression starts with "{operator}", which is not right!'

        for operator in operators:
            if request.endswith(operator):
                return f'Your expression ends with "{operator}", which is not right!'


class Handler2OperatorsChecker(AbstractHandler):
    """Checks, if equation has no more than 1x of each operator (not actually useful)"""

    def process_request(self, request):
        operators = {
            '/': 0,
            '*': 0,
            '-': 0,
            '+': 0
        }

        for operator in operators.keys():
            for symbol in request:
                if symbol == operator:
                    operators[operator] += 1

        for operator, count in operators.items():
            if count > 1:
                return f'Operator "{operator}" encountered more than once, which is not allowed!'


class Handler3ZeroDivision(AbstractHandler):
    """Checks if equation has division by 0"""

    def process_request(self, request):
        pattern = '/0'
        if re.findall(pattern, request):
            return f'Zero division is not mathematical!'


class Handler4Eval(AbstractHandler):
    """Main calculator logic"""

    def process_request(self, request):
        try:
            result = eval(request)
            return result
        except Exception as e:
            return f'Error occurred:\n{e}'
