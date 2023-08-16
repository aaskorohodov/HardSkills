from typing import Optional

from Interface import SearchEngine
from PATTERNS.Strategy import Strategies


class SearchApp:
    """Main class of a search application"""

    def __init__(self):
        self.words: list[str] = self.get_list_of_words()
        self.search_engines: list[SearchEngine] = self.create_engines()
        self.selected_engine: Optional[SearchEngine] = None

    def get_list_of_words(self) -> list[str]:
        """Opens file with english words (400+k), cleans, lowers, sorts and places it into pythonic list."""

        your_list = []
        with open('words.txt', 'r') as file:
            for word in file:
                word = word.strip()
                word = word.lower()
                your_list.append(word)

        your_list.sort()
        return your_list

    def create_engines(self) -> list[SearchEngine]:
        """Finds all classes in Strategies.py, checks if it derives from SearchEngine and initiates them all."""

        all_classes = dir(Strategies)
        search_engines = []

        for el in all_classes:
            cls = getattr(Strategies, el)

            try:
                if issubclass(cls, SearchEngine) and not cls == SearchEngine:
                    search_engines.append(cls())
            except:
                pass

        return search_engines

    def select_engine(self) -> None:
        """Gives user a way to select an engine via console, by typing its number."""

        number = 1
        comparison = {}
        for search_engine in self.search_engines:
            comparison[number] = search_engine
            number += 1

        print('Here are available Search Engines:')
        for num, se in comparison.items():
            print(f'{num}. {type(se).__name__} – {se.self_description}')

        engine_number = None
        selected_engine = None
        while not selected_engine:
            engine_number = input('\nSelect an engine, by typing its number:\n')
            try:
                engine_number = int(engine_number)
            except:
                pass

            if engine_number in comparison.keys():
                selected_engine = engine_number
            else:
                print(f'There is no engine №{engine_number}')

        print(f'You have selected engine "{type(comparison[engine_number]).__name__}"')
        self.selected_engine = comparison[engine_number]

    def search_word(self) -> None:
        """Searches a word through selected engine."""

        stop = False
        print('To stop type "Please stop it!"')
        while not stop:
            request = input('Enter a word to be searched:\n')

            if request.lower() == 'please stop it!':
                print('Goodbye!')
                exit()

            result = self.selected_engine.search(self.words, request)
            print(result)


app = SearchApp()
app.select_engine()
app.search_word()
