from abc import ABC, abstractmethod
from models import SocialNetworkUser

class ISocialNetwork(ABC):
    @abstractmethod
    def get_subscribers(self, user_name: str) -> list[SocialNetworkUser]:
        pass
