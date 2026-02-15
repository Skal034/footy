# Jersey logic: Iconic numbers prioritized for high-rated players
SHIRT_PREFS = {
    "GK": [1, 12, 13, 16, 25, 30, 31],
    "DEF": [2, 3, 4, 5, 6, 12, 14, 15, 22],
    "MID": [6, 8, 10, 14, 16, 17, 18, 20, 21, 23],
    "FWD": [7, 9, 10, 11, 19, 22, 29]
}

# Mapping specific positions to broader categories for jersey and attribute logic
POS_MAP = {
    "GK": "GK", "CB": "DEF", "LB": "DEF", "RB": "DEF",
    "DM": "MID", "CM": "MID", "AM": "MID",
    "LW": "FWD", "RW": "FWD", "ST": "FWD"
}

# Standardized attribute list to ensure every player row in the CSV has the same columns
ALL_ATTRIBUTES = [
    "Reflexes", "Positioning", "Handling", "Distribution", "Sweeping",
    "Acceleration", "Sprint_Speed", "Stamina", "Strength", "Jumping_Reach",
    "First_Touch", "Dribbling", "Short_Passing", "Long_Passing", "Finishing",
    "Tackling", "Attacking_Awareness", "Defensive_Awareness", "Composure", "Work_Rate"
]

import random
import teams
import config_reader as cfg
import asyncio
import inspect
import requests
from deep_translator import GoogleTranslator
from googletrans import Translator
from functools import lru_cache

translator = Translator()
# Safe translation helper: makes an async or sync `translate` call behave
# synchronously for callers here, with caching and a safe fallback.
@lru_cache(maxsize=1024)
def translate_to_en(text):
    try:
        res_or_coro = translator.translate(text, src='auto', dest='en')
        # If the library returns a coroutine (async implementation), fall back
        # to a synchronous HTTP request below to ensure completion.
        if inspect.isawaitable(res_or_coro):
            raise RuntimeError("async-translate")
        res = res_or_coro
        if res is None:
            return text
        return res.pronunciation
    except Exception:
        # Fallback: use unofficial Google Translate HTTP endpoint synchronously.
        """
        try:
            url = "https://translate.googleapis.com/translate_a/single"
            params = {
                'client': 'gtx', 'sl': 'auto', 'tl': 'en', 'dt': 't', 'q': text
            }
            resp = requests.get(url, params=params, timeout=5)
            resp.raise_for_status()
            data = resp.json()
            if data and isinstance(data, list) and data[0]:
                translated = ''.join([seg[0] for seg in data[0] if seg and seg[0]])
                return translated or text
        except Exception:
        """
        return GoogleTranslator(source='auto', target='en').translate(text)
    return text

class Player:
    def __init__(self, team_name, league_config, base_rating):
        self.team = team_name
        self.league = league_config['name']
        
        # Localized Player Nationality — bias selection by FIFA points and team quality
        # `_pick_nat` now returns a tuple: (country_name, locale_code)
        self.nationality, self.locale = self._pick_nat(league_config, base_rating)
        fk = teams.fake_factory.get(self.nationality, league_config['country'])
        
        # --- ENHANCED NAME GENERATION ---
        # We combine first_name_male and last_name to avoid "Dr.", "PhD", etc.
        self.name = f"{fk.first_name_male()} {fk.last_name()}"
        # Only attempt translation/romanization for locales likely to need it
        if self.locale in teams.locales_to_be_romanized:
            name = self.name
            # Try cached/safe translation; helper handles coroutine/sync differences
            translated = translate_to_en(name)
            self.name = translated
            #print(f"Transliterated from locale '{self.locale}' '{name}' to '{self.name}'.")

        self.age = random.randint(cfg.AGE_MIN, cfg.AGE_MAX)
        max_rating = cfg.MAX_BASE_RATING
        if (self.age < 18 or self.age > 37):
            max_rating = min(max_rating, 80)  # Young and old players capped at 80 OVR
        elif (self.age < 21 or self.age > 34):
            max_rating = min(max_rating, 85)  # Slightly younger and slightly older players capped at 85 OVR
        self.overall = max(cfg.MIN_BASE_RATING, 
                           min(max_rating, int(random.gauss(base_rating, 4))))
        self.position = random.choice(["GK"]*3 + ["CB", "LB", "RB"]*5 + ["DM", "CM", "AM"]*5 + ["LW", "RW", "ST"]*4)
        self.jersey = None
        
        # Meta Stats (The "3")
        self.meta = {
            "Weak_Foot": random.randint(1,5), 
            "Injury_Proneness": random.randint(0,100), 
            "Versatility": random.randint(0,100)
        }
        
        # Standardized Attributes (The 5/15) - Initialized to 0 to prevent CSV errors
        self.stats = {attr: 0 for attr in ALL_ATTRIBUTES}
        self._generate_stats(max_rating)

    def _pick_nat(self, conf, base_rating):
        """Pick a nationality biased by league local_weight and FIFA points.

        - With probability `local_weight` choose the league's country.
        - Otherwise pick a nationality from `locales` weighted by FIFA points,
          scaled by the team's base_rating so stronger teams more likely pick
          players from higher-ranked nations.
        """
        if random.random() < conf['local_weight']:
            country = conf['country']
            return country, teams.locales.get(country, {}).get('locale', 'en_GB')
        
        # Sort by normalized_rating in descending order
        normalized_locales = dict(sorted(
            teams.normalized_locales.items(), 
            key=lambda x: (x[1]['normalized_rating'] - base_rating) ** 2
        ))
        nations_list = list(normalized_locales.items())
        lambd = cfg.NATIONALITY_LAMBDA  # Adjust this to increase/decrease bias strength
        index = len(nations_list)
        while (index >= len(nations_list)):
            index = round(random.expovariate(lambd))
        nation, data = nations_list[index]
        return nation, data.get('locale', 'en_GB')

    def _generate_stats(self, max_rating):
        """Assigns ratings based on whether the player is a GK or Outfield player."""
        base = self.overall
        if self.position == "GK":
            for s in ["Reflexes", "Positioning", "Handling", "Distribution", "Sweeping"]:
                self.stats[s] = max(cfg.MIN_BASE_RATING, 
                                    min(max_rating, base + random.randint(-8, 8)))
        else:
            # Outfield stats are index 5 onwards in the ALL_ATTRIBUTES list
            for s in ALL_ATTRIBUTES[5:]:
                self.stats[s] = max(cfg.MIN_BASE_RATING, 
                                    min(max_rating, base + random.randint(-8, 8)))
            
            # Positional bias logic
            cat = POS_MAP[self.position]
            if cat == "DEF": 
                self.stats["Tackling"] += 10
                self.stats["Defensive_Awareness"] += 5
            if cat == "FWD": 
                self.stats["Finishing"] += 10
                self.stats["Attacking_Awareness"] += 5

    def to_dict(self):
        """Merges all player data into a single flat dictionary for CSV."""
        d = {
            "Name": self.name, "Team": self.team, "League": self.league, 
            "Nat": self.nationality, "Pos": self.position, "Age": self.age, 
            "OVR": self.overall, "Jersey": self.jersey
        }
        d.update(self.meta)
        d.update(self.stats)
        return d
