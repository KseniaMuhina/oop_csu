from external_libs.twitter_client import TwitterClient
from models import SocialNetworkUser
from social_networks.base import ISocialNetwork

class TwitterNetwork(ISocialNetwork):
    def __init__(self):
        self.client = TwitterClient()

    def get_subscribers(self, user_name: str) -> list[SocialNetworkUser]:
        user_id = self.client.get_user_id_by_name(user_name)
        raw_users = self.client.get_subscribers(user_id)
        return [SocialNetworkUser(self.client.get_user_name_by_id(u.user_id)) for u in raw_users]
