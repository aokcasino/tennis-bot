import random
from datetime import datetime
from requests_oauthlib import OAuth1Session

from content import PROGRAM_TEMPLATES, FUN_FACTS, ANALYSIS, SURFACE, CTA

API_KEY = "H1EALe1AG9MdN5lRhaGfvr4fp"
API_SECRET = "NJjTjsyA6MB8YXqyMY20ICvQ3Qohzeeya0vnzfre6uwiYO2QGf"
ACCESS_TOKEN = "4850639385-rpGLYM5KvnZeGNyYCJQOo8OPeF8fmEh9ZGwYpBh"
ACCESS_SECRET = "T238jt56gHTh8DDp8ABAEklwtGSg99m7AQhS01xE7DEKr"

# Mets ici les tournois ATP du moment à la main.
# Tu peux les changer chaque semaine.
CURRENT_TOURNAMENTS = [
    "Munich",
    "Barcelone"
]


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


def anti_duplicate_suffix() -> str:
    # Ajoute une petite variation pour éviter les doublons exacts sur X
    return f" ({get_day_label()} {datetime.now().strftime('%d/%m')})"


def build_program_tweet() -> str:
    tournaments = ", ".join(CURRENT_TOURNAMENTS)

    if tournaments.strip():
        intro = random.choice(PROGRAM_TEMPLATES).format(tournaments=tournaments)
    else:
        intro = "🎾 Plusieurs tournois ATP sont en cours cette semaine."

    tweet = f"{intro}{anti_duplicate_suffix()}"
    return tweet[:280]


def build_matchday_tweet() -> str:
    matchday_templates = [
        "🎾 Jour de match sur le circuit ATP. Dans ce genre de journée, la qualité de déplacement, la gestion des temps faibles et la constance au service peuvent faire basculer une rencontre.",
        "👀 Jour de match aujourd’hui : les écarts se font souvent sur les détails, surtout quand deux joueurs arrivent avec des dynamiques proches.",
        "📍 Jour de match ATP : certains profils entrent vite dans leur tournoi, tandis que d’autres ont besoin d’un set ou deux pour vraiment trouver leur rythme.",
        "🎾 Nouvelle journée de matchs ATP. Les premiers tours sont souvent plus piégeux qu’ils n’en ont l’air, car les repères récents ne racontent pas toujours toute l’histoire.",
        "📊 Jour de match sur le circuit : l’adaptation à la surface, la confiance actuelle et le contexte du tableau restent trois points très utiles à surveiller."
    ]

    tweet = f"{random.choice(matchday_templates)}{anti_duplicate_suffix()}"
    return tweet[:280]


def build_fun_fact_tweet() -> str:
    tweet = f"{random.choice(FUN_FACTS)}{anti_duplicate_suffix()}"
    return tweet[:280]


def build_analysis_tweet() -> str:
    tweet = f"{random.choice(ANALYSIS)}{anti_duplicate_suffix()}"
    return tweet[:280]


def build_surface_tweet() -> str:
    tweet = f"{random.choice(SURFACE)}{anti_duplicate_suffix()}"
    return tweet[:280]


def build_cta_tweet() -> str:
    tweet = f"{random.choice(CTA)}{anti_duplicate_suffix()}"
    return tweet[:280]


def main(mode: str = "program") -> None:
    if mode == "program":
        tweet = build_program_tweet()
    elif mode == "matchday":
        tweet = build_matchday_tweet()
    elif mode == "fact":
        tweet = build_fun_fact_tweet()
    elif mode == "analysis":
        tweet = build_analysis_tweet()
    elif mode == "surface":
        tweet = build_surface_tweet()
    elif mode == "cta":
        tweet = build_cta_tweet()
    else:
        tweet = build_program_tweet()

    print("Tweet choisi :", tweet)
    post_tweet(tweet)


if __name__ == "__main__":
    import sys

    mode = sys.argv[1] if len(sys.argv) > 1 else "program"
    main(mode)