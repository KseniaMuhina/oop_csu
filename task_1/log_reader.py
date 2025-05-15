from abc import ABC, abstractmethod

class ILogReader(ABC):
    @abstractmethod
    def read_log_file(self, identificator: str) -> str:
        pass

class FileLogReader(ILogReader):
    def read_log_file(self, identificator: str) -> str:
        return "FILE"
