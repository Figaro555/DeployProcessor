from abc import ABC, abstractmethod


class AbstractDataExtractor(ABC):
    @abstractmethod
    def get_data(self):
        pass