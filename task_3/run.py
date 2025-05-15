from services.vk_service import VkUserService
from services.twitter_service import TwitterUserService


def print_user_info(service, url):
    info = service.get_user_info(url)
    print(f"User: {info.name}, ID: {info.user_id}")
    print("Friends:")
    for f in info.friends:
        print(f" - {f.name} (ID: {f.user_id})")


if __name__ == "__main__":
    print("--- VK Example ---")
    print_user_info(VkUserService(), "https://vk.com/some_user")

    print("\n--- Twitter Example ---")
    print_user_info(TwitterUserService(), "https://twitter.com/someone")
