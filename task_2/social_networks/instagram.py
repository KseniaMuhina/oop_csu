from external_libs.instagram_client import InstagramClient
from models import SocialNetworkUser
from social_networks.base import ISocialNetwork

class InstagramNetwork(ISocialNetwork):
    def __init__(self):
        self.client = InstagramClient()

    def get_subscribers(self, user_name: str) -> list[SocialNetworkUser]:
        raw_users = self.client.get_subscribers(user_name)
        return [SocialNetworkUser(u.user_name) for u in raw_users]
