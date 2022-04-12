from abc import ABC, abstractmethod


class AbstractTransformer(ABC):
    @abstractmethod
    def transform_to_tuple(self, local_dl):
        pass
