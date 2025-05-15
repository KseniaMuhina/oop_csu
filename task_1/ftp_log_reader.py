from ftp_client import FtpClient
from log_reader import ILogReader

class FtpLogReader(ILogReader):
    def __init__(self, login: str, password: str):
        self._ftp_client = FtpClient()
        self._login = login
        self._password = password

    def read_log_file(self, identificator: str) -> str:
        path = identificator.replace("ftp://", "")
        return self._ftp_client.read_file(self._login, self._password, path)
