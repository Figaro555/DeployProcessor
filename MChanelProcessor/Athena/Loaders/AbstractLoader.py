from abc import ABC, abstractmethod


class AbstractLoader(ABC):
    @abstractmethod
    def load(self, list_to_load):
        pass
