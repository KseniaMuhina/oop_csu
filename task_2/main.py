from subscriber_viewer import SubscriberViewer
from social_networks.instagram import InstagramNetwork
from social_networks.twitter import TwitterNetwork

if __name__ == "__main__":
    user_name = "some_user"

    print("Instagram:")
    viewer = SubscriberViewer(InstagramNetwork())
    for user in viewer.get_subscribers(user_name):
        print(user.user_name)

    print("\nTwitter:")
    viewer = SubscriberViewer(TwitterNetwork())
    for user in viewer.get_subscribers(user_name):
        print(user.user_name)
