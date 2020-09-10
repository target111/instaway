from instagram_private_api import Client
import requests


class InstagramClient(object):
    def __init__(self, user: str, password: str) -> None:
        self.api = Client(user, password)

    def get_followers(self, user: str) -> list:
        followers = self.api.user_followers(user, self.api.uuid)
        return [user.get("username") for user in followers.get("users")]

    def post_comment(self, media_id: str, comment: str) -> None:
        self.api.post_comment(media_id, comment)

    def get_media_id(self, post_url: str) -> str:
        r = requests.get("https://api.instagram.com/oembed",
                         params={"url": post_url})
        return r.json().get("media_id")

    def get_user_id(self, user_url: str) -> str:
        r = requests.get(f"https://www.instagram.com/{user_url}/?__a=1")
        return r.json().get('graphql').get('user').get('id')
