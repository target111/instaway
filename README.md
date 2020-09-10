# InstaWay - Instagram Give-Away tagger
Tag all the followers of any given user in any Instagram give-away post.

## Command line options ##
```
./instaway.py -h
usage: instaway.py [-h] [-u USER_FOLLOWERS] [-t TIME_SLEEP TIME_SLEEP]
                   username password post_url

Instagram GiveAway Auto-Tagger.

positional arguments:
  username              Instagram username for authentication.
  password              Instagram password.
  post_url              URL of the giveaway post.

optional arguments:
  -h, --help            show this help message and exit
  -u USER_FOLLOWERS, --user-followers USER_FOLLOWERS
                        Tag all the followers of the specified username.
  -t TIME_SLEEP TIME_SLEEP, --time-sleep TIME_SLEEP TIME_SLEEP
                        Sleep interval to mimic a human operator (ex: -t 10
                        15).
```
