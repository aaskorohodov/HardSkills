from abc import ABC, abstractmethod
from typing import Optional


class SearchEngine(ABC):
    """Interface for specific implementations of search engine. Design to search words in a list of words"""

    @abstractmethod
    def __init__(self):
        self.self_description: Optional[str] = None

    @abstractmethod
    def search(self, search_in: list, search_this: str) -> str:
        """Logic of searching"""
        pass
