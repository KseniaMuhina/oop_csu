from models import SocialNetworkUser
from social_networks.base import ISocialNetwork

class SubscriberViewer:
    def __init__(self, social_network: ISocialNetwork):
        self.network = social_network

    def get_subscribers(self, user_name: str) -> list[SocialNetworkUser]:
        return self.network.get_subscribers(user_name)
