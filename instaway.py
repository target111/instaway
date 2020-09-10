from lib.client import InstagramClient
from lib.utils import sleep_random
import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Instagram GiveAway Auto-Tagger.")
    parser.add_argument(
        "username",
        type=str,
        help="Instagram username for authentication.")
    parser.add_argument(
        "password",
        type=str,
        help="Instagram password.")
    parser.add_argument(
        "post_url",
        type=str,
        help="URL of the giveaway post.")
    parser.add_argument(
        "-u",
        "--user-followers",
        type=str,
        help="Tag all the followers of the specified username.")
    parser.add_argument(
        "-t",
        "--time-sleep",
        type=int,
        nargs=2,
        help="Sleep interval to mimic a human operator (ex: -t 10 15).")

    return parser.parse_args()


def run(args=None) -> None:
    api = InstagramClient(args.username, args.password)
    media_id = api.get_media_id(args.post_url)

    user = api.get_user_id(
        args.user_followers) if args.user_followers else api.authenticated_user_ide
    followers = api.get_followers(user)

    for follower in followers:
        api.post_comment(media_id, f'@{follower}')
        print(f'Tagged: {follower}')

        if args.time_sleep:
            sleep_random(tuple(args.time_sleep))


def main() -> None:
    run(parse_args())


if __name__ == "__main__":
    main()
