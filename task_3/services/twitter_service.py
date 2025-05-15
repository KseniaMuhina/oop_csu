from core.base_service import BaseUserService
from core.models import UserInfo
import re


class TwitterUser:
    def __init__(self, user_id):
        self.user_id = user_id


class FakeTwitterClient:
    def get_subscribers(self, user_id):
        return [TwitterUser(101), TwitterUser(102)]

    def get_user_name_by_id(self, user_id):
        return f"TwitterUser{user_id}"


class TwitterUserService(BaseUserService):
    def __init__(self):
        self.client = FakeTwitterClient()

    def parse_url(self, page_url: str) -> str:
        match = re.search(r"twitter.com/(\w+)", page_url)
        return self.get_user_id(match.group(1))

    def get_user_id(self, user_name: str) -> str:
        return "tw_user_42"

    def get_name(self, user_id: str) -> str:
        return "Twitter Name"

    def get_friends(self, user_id: str):
        return self.client.get_subscribers(user_id)

    def convert_friends(self, raw_friends) -> list:
        return [UserInfo(
            name=self.client.get_user_name_by_id(u.user_id),
            user_id=str(u.user_id),
            friends=[]
        ) for u in raw_friends]
