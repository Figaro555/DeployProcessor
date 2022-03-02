from abc import ABC, abstractmethod


class AbstractTransformer(ABC):
    @abstractmethod
    def transform_to_local_array(self, local_dl):
        pass
