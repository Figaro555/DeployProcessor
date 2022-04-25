from abc import ABC, abstractmethod
from time import time


class AbstractConnector(ABC):
    @abstractmethod
    def create_connection(self):
        pass

    def get_connection(self):
        if abs(time() - self.last_connection_update) > 3 * 60:
            self.last_connection_update = time()

            try:
                self.connection = self.create_connection()
                return self.connection

            except Exception as _ex:
                print("[ERROR] Error while creating connection " + self.type, _ex)

        return self.connection