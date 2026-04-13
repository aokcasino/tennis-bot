import random
from datetime import datetime
from requests_oauthlib import OAuth1Session

from content import MATCHDAY, FACTS, SURFACE, ANALYSIS, CTA


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


def get_day_label() -> str:
    days = {
        0: "lundi",
        1: "mardi",
        2: "mercredi",
        3: "jeudi",
        4: "vendredi",
        5: "samedi",
        6: "dimanche",
    }
    return days[datetime.now().weekday()]


def anti_duplicate_suffix(mode: str = "") -> str:
    return f" • {mode} • {get_day_label()} {datetime.now().strftime('%d/%m %H:%M')}"


def build_matchday_tweet() -> str:
    tweet = f"{random.choice(MATCHDAY)}{anti_duplicate_suffix('matchday')}"
    return tweet[:280]


def build_fact_tweet() -> str:
    tweet = f"{random.choice(FACTS)}{anti_duplicate_suffix('fact')}"
    return tweet[:280]


def build_analysis_tweet() -> str:
    pool = ANALYSIS + SURFACE
    tweet = f"{random.choice(pool)}{anti_duplicate_suffix('analysis')}"
    return tweet[:280]


def build_cta_tweet() -> str:
    tweet = f"{random.choice(CTA)}{anti_duplicate_suffix('cta')}"
    return tweet[:280]


def main(mode: str = "analysis") -> None:
    if mode == "matchday":
        tweet = build_matchday_tweet()
    elif mode == "fact":
        tweet = build_fact_tweet()
    elif mode == "analysis":
        tweet = build_analysis_tweet()
    elif mode == "cta":
        tweet = build_cta_tweet()
    else:
        tweet = build_analysis_tweet()

    print("Tweet choisi :", tweet)
    post_tweet(tweet)


if __name__ == "__main__":
    import sys

    mode = sys.argv[1] if len(sys.argv) > 1 else "analysis"
    main(mode)
