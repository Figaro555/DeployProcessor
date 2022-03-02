from abc import ABC, abstractmethod


class AbstractDataGetter(ABC):
    @abstractmethod
    def get_data(self):
        pass