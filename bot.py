import random
import sys
from requests_oauthlib import OAuth1Session

from content import TWEETS_WITH_HASHTAGS


API_KEY = "H1EALe1AG9MdN5lRhaGfvr4fp"
API_SECRET = "NJjTjsyA6MB8YXqyMY20ICvQ3Qohzeeya0vnzfre6uwiYO2QGf"
ACCESS_TOKEN = "4850639385-rpGLYM5KvnZeGNyYCJQOo8OPeF8fmEh9ZGwYpBh"
ACCESS_SECRET = "T238jt56gHTh8DDp8ABAEklwtGSg99m7AQhS01xE7DEKr"


def post_tweet(text: str) -> None:
    url = "https://api.x.com/2/tweets"

    oauth = OAuth1Session(
        client_key=API_KEY,
        client_secret=API_SECRET,
        resource_owner_key=ACCESS_TOKEN,
        resource_owner_secret=ACCESS_SECRET,
    )

    response = oauth.post(
        url,
        json={"text": text[:280]},
        headers={"Content-Type": "application/json"},
        timeout=30,
    )

    print("STATUS:", response.status_code)
    print("BODY:", response.text)
    response.raise_for_status()


def build_tweet() -> str:
    if not TWEETS_WITH_HASHTAGS:
        raise ValueError("La liste TWEETS_WITH_HASHTAGS est vide dans content.py")

    tweet = random.choice(TWEETS_WITH_HASHTAGS).strip()

    if not tweet:
        raise ValueError("Un tweet vide a été trouvé dans content.py")

    return tweet[:280]


def main() -> None:
    try:
        tweet = build_tweet()
        print("Tweet choisi :")
        print(tweet)
        post_tweet(tweet)
        print("Tweet publié avec succès.")
    except Exception as e:
        print(f"Erreur : {e}")
        raise


if __name__ == "__main__":
    main()
