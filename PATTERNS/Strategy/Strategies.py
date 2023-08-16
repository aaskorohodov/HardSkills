import random
import time

from Interface import SearchEngine


class Bisect(SearchEngine):
    def __init__(self):
        self.self_description = 'This is a pretty fast bisect search engin. It works by dividing a set into two pieces,' \
                                ' and trying to find a place to put given data in. It only works with sorted data-set.'

    def search(self, search_in, search_this):
        import bisect

        time_start = time.time()
        time.time()
        index = bisect.bisect(search_in, search_this)
        time_end = time.time()
        time_spend = time_end - time_start

        if search_in[index - 1] == search_this:
            return f'Index == {index - 1}\n' \
                   f'Time spend == {time_spend}'

        else:
            return f'No word {search_this} found!\n' \
                   f'Time spend = {time_spend}'


class RandomSearch(SearchEngine):
    def __init__(self):
        self.self_description = 'This is a random search engine, which randomly picks up an element in data-set, untill' \
                                ' until it finds what we are looking for.'

    def search(self, search_in, search_this):
        # If there is no such word in a given list, search will go endlessly. We do not want that
        if search_this not in search_in:
            return f'Word {search_this} is not in searchable!'

        indexes = [i for i in range(len(search_in))]
        time_start = time.time()
        index = None

        found = False
        while not found:
            index = random.choice(indexes)
            word = search_in[index]
            if word == search_this:
                found = True

        time_end = time.time()
        time_spend = time_end - time_start
        return f'Index == {index}\n' \
               f'Time spend == {time_spend}'


class PythonSearch(SearchEngine):
    def __init__(self):
        self.self_description = 'This is a standard pythonic search with the help of ".index()" function.'

    def search(self, search_in, search_this):
        time_start = time.time()
        try:
            index = search_in.index(search_this)
            time_end = time.time()
            time_spend = time_end - time_start
            return f'Index == {index}\n' \
                   f'Time spend == {time_spend}'

        except ValueError:
            time_end = time.time()
            time_spend = time_end - time_start
            return f'Word {search_this} is not in searchable!\n' \
                   f'Time spend == {time_spend}'


class LinearSearch(SearchEngine):
    def __init__(self):
        self.self_description = 'This is a linear search, in which we picking up element by element, until we find ' \
                                'what we were looking for'

    def search(self, search_in, search_this):
        time_start = time.time()

        for index in range(len(search_in)):
            el = search_in[index]
            if el == search_this:
                time_end = time.time()
                time_spend = time_end - time_start
                return f'Index == {index}\n' \
                       f'Time spend == {time_spend}'

        time_end = time.time()
        time_spend = time_end - time_start
        return f'Word {search_this} is not in searchable!\n' \
               f'Time spend == {time_spend}'
