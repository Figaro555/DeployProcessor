from abc import ABC, abstractmethod


class AbstractDataSerializator(ABC):
    @abstractmethod
    def serialize(self):
        pass
