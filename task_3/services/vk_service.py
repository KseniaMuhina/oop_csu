from core.base_service import BaseUserService
from core.models import UserInfo


class VkUser:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


class VkUserService(BaseUserService):
    def parse_url(self, page_url: str) -> str:
        return "vk_user_id_extracted"

    def get_name(self, user_id: str) -> str:
        return "VK User Name"

    def get_friends(self, user_id: str):
        return [VkUser("vk_friend_1", "VK Friend One"),
                VkUser("vk_friend_2", "VK Friend Two")]

    def convert_friends(self, raw_friends) -> list:
        return [UserInfo(name=u.name, user_id=u.user_id, friends=[]) for u in raw_friends]
