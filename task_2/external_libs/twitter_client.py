class TwitterUser:
    def __init__(self, user_id: int):
        self.user_id = user_id


class TwitterClient:
    def get_user_id_by_name(self, name: str) -> int:
        return 1  # Мок: просто фейковый ID

    def get_user_name_by_id(self, user_id: int) -> str:
        return f"twitter_user_{user_id}"

    def get_subscribers(self, user_id: int) -> list[TwitterUser]:
        return [TwitterUser(101), TwitterUser(102)]
