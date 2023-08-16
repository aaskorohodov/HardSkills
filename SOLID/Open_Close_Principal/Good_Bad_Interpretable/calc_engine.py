from abc import abstractmethod
from typing import Optional


class CalcEngine:
    """Abstract class for different calculations operators (/*-+ etc)"""

    def __init__(self, expression: str, command: str):
        self.expression:    str = expression
        self.command:       str = command
        self.result:        Optional[int] = None
        self.operators =    ['*', '/', '-', '+']

    @abstractmethod
    def calculate(self):
        pass

    def verify_rounding(self, number) -> int or float:
        """Rounds a given number, if it's fractional part is 0

        Example:
            100.0 -> 100
            100.1 -> 100.1
            100.01 -> 100.01"""

        if round(float(number)) == float(number):
            return round(float(number))
        else:
            return float(number)

    def find_operator(self) -> str:
        """Finds operator (/*-+) in expression.

        If expression has two operators, which possible only if there is a negative symbol in front of first number
        (and there is two numbers), than returns operator, rather than '-'

        Example:
            100-50  -> '-'
            100*50  -> '*'
            -100    -> '-'
            -100*50 -> '*'
            -10-10  -> '-'"""

        minus_operator = None
        operator = None

        for el in self.operators:
            if el in self.expression:
                if el == '-':
                    minus_operator = '-'
                else:
                    operator = el

        if not operator:
            return minus_operator
        else:
            return operator


class BasicOperations(CalcEngine):
    """Performs 4 basic operations: /*-+"""

    def calculate(self) -> str:
        try:
            result = eval(self.expression)
        except Exception as e:
            if isinstance(e, ZeroDivisionError):
                return f'0{self.command}'
            for el in self.operators:
                if self.expression.endswith(el):
                    return f'{self.expression[:-1]}{self.command}'
            return f'{self.expression}{self.command}'
        return f'{result}{self.command}'


class Square(CalcEngine):
    """Squares the last number of the expression.

    Example:
        10 + 10 -> 10 + 100
        10      -> 100"""

    def calculate(self):
        """Finds out, if any operator was applied to expression, and if so, then finds where the number/numbers
        in expression is, squares the last one (or the only one) number."""

        # Finding if any operator (/*-+...) was applied
        operator = self.find_operator()

        # Expression could be (10+10).split('+')->['10','10'] or (10+).split('+')->['10','']...
        if operator:
            first_numb = self.expression.split(operator)[0]     # ...thus this would be '10'
            second_num = self.expression.split(operator)[-1]    # ...thus this could be '10' or ''

            # If second_num is a number, rather than ''
            if second_num and first_numb:
                second_num_squared = str(eval(f'{second_num}*{second_num}'))
                return f'{first_numb}{operator}{second_num_squared}'
            if second_num and not first_numb:
                second_num_squared = str(eval(f'{second_num}*{second_num}'))
                return str(second_num_squared)
            # If second_num is ''
            if first_numb:
                return str(eval(f'{first_numb}*{first_numb}'))
        else:
            return str(eval(f'{self.expression}*{self.expression}'))


class Percent(CalcEngine):
    """Calculates percent of any number in expression

    Example:
        200 - 1% = 200 - 2
        200 * 50% = 200 * 100

    If user tries to calculate percent not from expression, but from a single number (50%) -> returns ''
    Because we can't calculate 50% from nothing."""

    def calculate(self):
        # Finds operator in expression (/*-+)
        operator = self.find_operator()

        if operator:
            first_num = self.expression.split(operator)[0]
            second_num = self.expression.split(operator)[-1]

            # first or second numbers could be '', if expression was (-50)
            if second_num and first_num and first_num not in self.operators:
                second_num_percented = eval(first_num) / 100 * eval(second_num)
                second_num_percented = self.verify_rounding(second_num_percented)
                return f'{first_num}{operator}{second_num_percented}'

            else:
                return ''


class PlusMinus(CalcEngine):
    """Reverses positive number to negative and vice versa. Reverse only the last number if expression."""

    def calculate(self) -> str:
        """Works primarily with .split() – splitting expression by operator, gives us left and right number.
        Difficulties begin, when we have more than one operator (-10*10 or -10-10).
        Fucking mess."""

        # Empty expression protection
        if self.expression == '':
            return ''

        operator = self.find_operator()

        if operator:
            first_num = None
            second_num = None

            '''If there is more than one "-" – after splitting number would not be in list[0], rather than list[1]'''
            if operator == '-':
                counter = 0
                for el in self.expression:
                    if el == '-':
                        counter += 1

                if counter == 2:
                    first_num = self.expression.split(operator)[1]
                    second_num = self.expression.split(operator)[-1]
                else:
                    first_num = self.expression.split(operator)[0]
                    second_num = self.expression.split(operator)[-1]

            if not first_num and not second_num:
                first_num = self.expression.split(operator)[0]
                second_num = self.expression.split(operator)[-1]

            if second_num and first_num:
                second_num_float = float(second_num)
                second_num_rounded = self.verify_rounding(second_num_float)
                if second_num_rounded < 0:
                    return f'{first_num}{operator}{second_num_rounded * -1}'
                if second_num_rounded > 0:
                    result = eval(f'{first_num}{operator}{second_num_rounded * -1}')
                    return str(result)
                if second_num_rounded == 0:
                    return f'{first_num}{operator}{0}'

            if not first_num and second_num:
                second_num_rounded = self.verify_rounding(second_num)
                return f'{second_num_rounded}'
            return f'{self.expression}'
        else:
            rounded_num = self.verify_rounding(self.expression)
            return f'{rounded_num * -1}'


class Equal(CalcEngine):
    """Handles button '='"""

    def calculate(self) -> str:
        if self.expression:
            try:
                result = eval(f'{self.expression}')
            except ZeroDivisionError:
                return '0'
            rounded_result = self.verify_rounding(result)
            return str(rounded_result)
