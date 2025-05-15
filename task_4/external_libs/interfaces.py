from abc import ABC, abstractmethod

class IDatabaseSaver(ABC):
    @abstractmethod
    def save_data(self, data):
        pass
