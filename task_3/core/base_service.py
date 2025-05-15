from abc import ABC, abstractmethod
from core.models import UserInfo


class BaseUserService(ABC):
    def get_user_info(self, page_url: str) -> UserInfo:
        user_id = self.parse_url(page_url)
        name = self.get_name(user_id)
        raw_friends = self.get_friends(user_id)
        friends = self.convert_friends(raw_friends)
        return UserInfo(name=name, user_id=user_id, friends=friends)

    @abstractmethod
    def parse_url(self, page_url: str) -> str:
        pass

    @abstractmethod
    def get_name(self, user_id: str) -> str:
        pass

    @abstractmethod
    def get_friends(self, user_id: str):
        pass

    @abstractmethod
    def convert_friends(self, raw_friends) -> list:
        pass
