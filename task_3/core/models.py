from dataclasses import dataclass
from typing import List


@dataclass
class UserInfo:
    name: str
    user_id: str
    friends: List['UserInfo']
