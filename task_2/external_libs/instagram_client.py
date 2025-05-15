class InstagramUser:
    def __init__(self, user_name: str):
        self.user_name = user_name


class InstagramClient:
    def get_subscribers(self, user_name: str) -> list[InstagramUser]:
        # Мок: возвращает список фейковых подписчиков
        return [InstagramUser("insta_fan1"), InstagramUser("insta_fan2")]
