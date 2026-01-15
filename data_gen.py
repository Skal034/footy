import random
import csv
import asyncio
from faker import Faker
from deep_translator import GoogleTranslator

# --- 1. LOCALIZED FACTORY SETUP ---
# Locales for Player names and Team cities
locales = {
    # Core footballing countries (kept original keys for compatibility)
    # Each entry: { 'locale': <faker_locale>, 'fifa': <points> }
    'England': {'locale': 'en_GB', 'fifa': 1834.12},
    'Spain': {'locale': 'es_ES', 'fifa': 1877.18},
    'USA': {'locale': 'en_US', 'fifa': 1681.88},
    'India': {'locale': 'en_IN', 'fifa': 1200},
    'Brazil': {'locale': 'pt_BR', 'fifa': 1760.46},
    'France': {'locale': 'fr_FR', 'fifa': 1870.00},
    'Germany': {'locale': 'de_DE', 'fifa': 1724.15},
    'Argentina': {'locale': 'es_AR', 'fifa': 1873.33},
    'Italy': {'locale': 'it_IT', 'fifa': 1702.06},
    'Netherlands': {'locale': 'nl_NL', 'fifa': 1756.27},

    # Expanded list — FIFA points default to 1200 where unknown
    'Portugal': {'locale': 'pt_PT', 'fifa': 1760.38}, 'Belgium': {'locale': 'nl_NL', 'fifa': 1730.71},
    'Sweden': {'locale': 'sv_SE', 'fifa': 1487.13}, 'Norway': {'locale': 'no_NO', 'fifa': 1553.14},
    'Denmark': {'locale': 'da_DK', 'fifa': 1616.75}, 'Finland': {'locale': 'fi_FI', 'fifa': 1200},
    'Russia': {'locale': 'ru_RU', 'fifa': 1524.52}, 'Ukraine': {'locale': 'ru_RU', 'fifa': 1557.47},
    'Poland': {'locale': 'pl_PL', 'fifa': 1532.04}, 'Czechia': {'locale': 'cs_CZ', 'fifa': 1487.00},
    'Slovakia': {'locale': 'pl_PL', 'fifa': 1485.65}, 'Hungary': {'locale': 'pl_PL', 'fifa': 1200},
    'Romania': {'locale': 'pl_PL', 'fifa': 1465.78}, 'Bulgaria': {'locale': 'pl_PL', 'fifa': 1200},
    'Greece': {'locale': 'en_GB', 'fifa': 1480.38}, 'Turkey': {'locale': 'en_GB', 'fifa': 1582.69},
    'Japan': {'locale': 'ja_JP', 'fifa': 1650.12}, 'South Korea': {'locale': 'ko_KR', 'fifa': 1599.45},
    'China': {'locale': 'zh_CN', 'fifa': 1200}, 'Taiwan': {'locale': 'zh_TW', 'fifa': 1200},
    'Vietnam': {'locale': 'zh_CN', 'fifa': 1200}, 'Thailand': {'locale': 'zh_CN', 'fifa': 1200},
    'Indonesia': {'locale': 'id_ID', 'fifa': 1200}, 'Malaysia': {'locale': 'en_US', 'fifa': 1200},
    'Philippines': {'locale': 'en_US', 'fifa': 1200}, 'Bangladesh': {'locale': 'bn_BD', 'fifa': 1200},
    'Pakistan': {'locale': 'en_PK', 'fifa': 1200}, 'Sri Lanka': {'locale': 'en_GB', 'fifa': 1200},
    'Nepal': {'locale': 'en_GB', 'fifa': 1200}, 'Australia': {'locale': 'en_AU', 'fifa': 1574.01},
    'New Zealand': {'locale': 'en_NZ', 'fifa': 1200}, 'Canada': {'locale': 'en_CA', 'fifa': 1559.15},
    'Mexico': {'locale': 'es_MX', 'fifa': 1675.75}, 'Colombia': {'locale': 'es_ES', 'fifa': 1701.30},
    'Chile': {'locale': 'es_CL', 'fifa': 1200}, 'Peru': {'locale': 'es_ES', 'fifa': 1200},
    'Uruguay': {'locale': 'es_AR', 'fifa': 1672.62}, 'Paraguay': {'locale': 'es_ES', 'fifa': 1501.50},
    'Bolivia': {'locale': 'es_ES', 'fifa': 1200}, 'Ecuador': {'locale': 'es_ES', 'fifa': 1591.73},
    'Venezuela': {'locale': 'es_ES', 'fifa': 1465.22}, 'Costa Rica': {'locale': 'es_ES', 'fifa': 1464.24},
    'Panama': {'locale': 'es_ES', 'fifa': 1540.43}, 'Honduras': {'locale': 'es_ES', 'fifa': 1200},
    'Guatemala': {'locale': 'es_ES', 'fifa': 1200}, 'El Salvador': {'locale': 'es_ES', 'fifa': 1200},
    'Nicaragua': {'locale': 'es_ES', 'fifa': 1200}, 'Dominican Republic': {'locale': 'es_ES', 'fifa': 1200},
    'Cuba': {'locale': 'es_ES', 'fifa': 1200}, 'Jamaica': {'locale': 'en_US', 'fifa': 1200},
    'Trinidad and Tobago': {'locale': 'en_US', 'fifa': 1200}, 'Haiti': {'locale': 'fr_FR', 'fifa': 1200},

    # Balkans and nearby (mapped to stable locales)
    'Belarus': {'locale': 'ru_RU', 'fifa': 1200}, 'Serbia': {'locale': 'en_GB', 'fifa': 1506.34},
    'Croatia': {'locale': 'en_GB', 'fifa': 1716.88}, 'Slovenia': {'locale': 'en_GB', 'fifa': 1200},
    'Bosnia and Herzegovina': {'locale': 'en_GB', 'fifa': 1200}, 'North Macedonia': {'locale': 'en_GB', 'fifa': 1200},
    'Albania': {'locale': 'en_GB', 'fifa': 1200}, 'Montenegro': {'locale': 'en_GB', 'fifa': 1200},
    'Kosovo': {'locale': 'en_GB', 'fifa': 1200},

    # Middle East & North Africa (mapped conservatively)
    'Israel': {'locale': 'en_GB', 'fifa': 1200}, 'Palestine': {'locale': 'en_GB', 'fifa': 1200},
    'Saudi Arabia': {'locale': 'en_PK', 'fifa': 1200}, 'UAE': {'locale': 'en_GB', 'fifa': 1200},
    'Qatar': {'locale': 'en_PK', 'fifa': 1200}, 'Kuwait': {'locale': 'en_GB', 'fifa': 1200},
    'Bahrain': {'locale': 'en_GB', 'fifa': 1200}, 'Oman': {'locale': 'en_GB', 'fifa': 1200},
    'Jordan': {'locale': 'en_GB', 'fifa': 1200}, 'Lebanon': {'locale': 'fr_FR', 'fifa': 1200},
    'Iraq': {'locale': 'en_GB', 'fifa': 1200}, 'Iran': {'locale': 'en_GB', 'fifa': 1617.02},
    'Egypt': {'locale': 'fr_FR', 'fifa': 1515.18}, 'Morocco': {'locale': 'en_PK', 'fifa': 1716.34},
    'Algeria': {'locale': 'fr_FR', 'fifa': 1517.68}, 'Tunisia': {'locale': 'fr_FR', 'fifa': 1494.86},

    # Africa (mapped to common locales)
    'South Africa': {'locale': 'en_GB', 'fifa': 1200}, 'Nigeria': {'locale': 'en_KE', 'fifa': 1502.46},
    'Ghana': {'locale': 'en_KE', 'fifa': 1200}, 'Cameroon': {'locale': 'en_KE', 'fifa': 1200},
    'Senegal': {'locale': 'fr_FR', 'fifa': 1648.07}, 'Ivory Coast': {'locale': 'fr_FR', 'fifa': 1489.59},
    'Congo': {'locale': 'fr_FR', 'fifa': 1200}, 'DR Congo': {'locale': 'fr_FR', 'fifa': 1200},
    'Ethiopia': {'locale': 'en_GB', 'fifa': 1200}, 'Kenya': {'locale': 'en_GB', 'fifa': 1200},
    'Uganda': {'locale': 'en_GB', 'fifa': 1200}, 'Zambia': {'locale': 'en_GB', 'fifa': 1200},
    'Zimbabwe': {'locale': 'en_GB', 'fifa': 1200},

    # Smaller football nations and regions
    'Iceland': {'locale': 'en_GB', 'fifa': 1200}, 'Luxembourg': {'locale': 'fr_FR', 'fifa': 1200},
    'Malta': {'locale': 'en_GB', 'fifa': 1200}, 'Cyprus': {'locale': 'en_GB', 'fifa': 1200},
    'Azerbaijan': {'locale': 'ru_RU', 'fifa': 1200}, 'Georgia': {'locale': 'ru_RU', 'fifa': 1200},
    'Armenia': {'locale': 'ru_RU', 'fifa': 1200}, 'Kazakhstan': {'locale': 'ru_RU', 'fifa': 1200},
    'Uzbekistan': {'locale': 'ru_RU', 'fifa': 1462.03}, 'Kyrgyzstan': {'locale': 'ru_RU', 'fifa': 1200},
    'Tajikistan': {'locale': 'ru_RU', 'fifa': 1200}, 'Mongolia': {'locale': 'en_GB', 'fifa': 1200},

    # Caribbean & Central America
    'Bahamas': {'locale': 'en_US', 'fifa': 1200}, 'Barbados': {'locale': 'en_US', 'fifa': 1200},
    'Saint Lucia': {'locale': 'en_US', 'fifa': 1200}, 'Grenada': {'locale': 'en_US', 'fifa': 1200},
    'Antigua and Barbuda': {'locale': 'en_US', 'fifa': 1200}, 'Saint Kitts and Nevis': {'locale': 'en_US', 'fifa': 1200},

    # Oceania
    'Fiji': {'locale': 'en_AU', 'fifa': 1200}, 'Solomon Islands': {'locale': 'en_AU', 'fifa': 1200},

    # Extra mappings to ensure broad diversity (uses stable Faker locales)
    'Scotland': {'locale': 'en_GB', 'fifa': 1506.77}, 'Wales': {'locale': 'en_GB', 'fifa': 1529.71},
    'Northern Ireland': {'locale': 'en_GB', 'fifa': 1200}, 'Ireland': {'locale': 'en_GB', 'fifa': 1580.12}
}

# Build Faker factories from the locale definitions
fake_factory = {nation: Faker(info['locale']) for nation, info in locales.items()}

# Helper: numeric FIFA points for each locale (extracted from locales)
fifa_points = {nation: info.get('fifa', 1200) for nation, info in locales.items()}

# --- 2. CONFIGURATION ---

LEAGUES = {
    "ENG_1": {"name": "Premier League", "country": "England", "tier": 1, "teams": 20, "local_weight": 0.45},
    "ESP_1": {"name": "La Liga", "country": "Spain", "tier": 1, "teams": 20, "local_weight": 0.65},
    "USA_1": {"name": "MLS", "country": "USA", "tier": 2, "teams": 18, "local_weight": 0.55},
    "IND_1": {"name": "Indian Super League", "country": "India", "tier": 3, "teams": 12, "local_weight": 0.85},
}

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

# --- 3. LOGIC ENGINES ---

def generate_league_team_names(country, count):
    """Generates unique team names based on country geography and local naming styles."""
    names = set()
    fk = fake_factory.get(country, fake_factory['England'])
    
    cities = []
    while len(set(cities)) < count:
        cities.append(fk.city())
    cities = list(set(cities))

    for city in cities:
        if country == "Spain":
            prefixes = ["Real", "Atlético", "Deportivo"]
            name = f"{random.choice(prefixes)} {city}" if random.random() > 0.4 else f"{city} CF"
        elif country == "USA" and random.random() > 0.7:
            name = f"{city} {fk.last_name()}s" 
        else:
            suffixes = ["United", "City", "Town", "Rovers", "Athletic", "FC"]
            name = f"{city} {random.choice(suffixes)}"
        names.add(name)
    return list(names)[:count]

class Player:
    def __init__(self, team_name, league_config, base_rating):
        self.team = team_name
        self.league = league_config['name']
        
        # Localized Player Nationality — bias selection by FIFA points and team quality
        # `_pick_nat` now returns a tuple: (country_name, locale_code)
        self.nationality, self.locale = self._pick_nat(league_config, base_rating)
        fk = fake_factory.get(self.nationality, fake_factory['England'])
        
        # --- ENHANCED NAME GENERATION ---
        # We combine first_name_male and last_name to avoid "Dr.", "PhD", etc.
        self.name = f"{fk.first_name_male()} {fk.last_name()}"
        # Only attempt translation/romanization for locales likely to need it
        if self.locale in ("ja_JP", "ko_KR", "zh_CN", "zh_TW", "bn_BD"):
            self.name = GoogleTranslator(source='auto', target='en').translate(self.name)
        
        self.age = random.randint(16, 40)
        self.overall = max(40, min(99, int(random.gauss(base_rating, 4))))
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
        self._generate_stats()

    def _pick_nat(self, conf, base_rating):
        """Pick a nationality biased by league local_weight and FIFA points.

        - With probability `local_weight` choose the league's country.
        - Otherwise pick a nationality from `locales` weighted by FIFA points,
          scaled by the team's base_rating so stronger teams more likely pick
          players from higher-ranked nations.
        """
        if random.random() < conf['local_weight']:
            country = conf['country']
            return country, locales.get(country, {}).get('locale', 'en_GB')

        nations = list(locales.keys())
        # base multiplier: teams with higher base_rating slightly favour top nations
        base_mult = 1.0 + ((base_rating - 60) / 100.0)
        weights = [max(1.0, fifa_points.get(n, 1200) * base_mult) for n in nations]
        total = sum(weights)
        # normalized selection
        r = random.random() * total
        upto = 0.0
        for n, w in zip(nations, weights):
            upto += w
            if r <= upto:
                return n, locales.get(n, {}).get('locale', 'en_GB')
        last = nations[-1]
        return last, locales.get(last, {}).get('locale', 'en_GB')

    def _generate_stats(self):
        """Assigns ratings based on whether the player is a GK or Outfield player."""
        base = self.overall
        if self.position == "GK":
            for s in ["Reflexes", "Positioning", "Handling", "Distribution", "Sweeping"]:
                self.stats[s] = max(1, min(99, base + random.randint(-5, 10)))
        else:
            # Outfield stats are index 5 onwards in the ALL_ATTRIBUTES list
            for s in ALL_ATTRIBUTES[5:]:
                self.stats[s] = max(1, min(99, base + random.randint(-8, 8)))
            
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

class Team:
    def __init__(self, name, config, s_tier):
        self.name = name
        # Quality tiers (1: Top, 2: Mid, 3: Bottom) mapped to OVR
        qualities = {1: [85, 78, 72], 2: [75, 68, 62], 3: [64, 58, 52]}
        base_ovr = qualities[config['tier']][s_tier - 1]
        
        # 30 players per squad
        self.players = [Player(self.name, config, base_ovr + random.randint(-3, 3)) for _ in range(30)]
        self._assign_jerseys()

    def _assign_jerseys(self):
        """Star players get priority for iconic numbers; no duplicates allowed."""
        used = set()
        # High-rated players pick first
        for p in sorted(self.players, key=lambda x: x.overall, reverse=True):
            cat = POS_MAP[p.position]
            assigned = False
            for num in SHIRT_PREFS[cat]:
                if num not in used:
                    p.jersey = num
                    used.add(num)
                    assigned = True
                    break
            
            if not assigned:
                while True:
                    rand_num = random.randint(1, 99)
                    if rand_num not in used:
                        p.jersey = rand_num
                        used.add(rand_num)
                        break

# --- 4. EXECUTION ---

if __name__ == "__main__":
    full_db = []
    print("Generating localized football universe...")
    
    for l_id, conf in LEAGUES.items():
        print(f"-> {conf['name']} ({conf['country']})")
        team_names = generate_league_team_names(conf['country'], conf['teams'])
        
        for i, t_name in enumerate(team_names):
            # Roughly distribute team strengths
            s_tier = 1 if i < 3 else (3 if i > (conf['teams'] - 5) else 2)
            team_obj = Team(t_name, conf, s_tier)
            full_db.extend([p.to_dict() for p in team_obj.players])

    # Save to CSV using the keys of the first entry as headers
    field_names = list(full_db[0].keys())
    with open("data.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(full_db)

    print(f"\nSuccess! 'data.csv' created with {len(full_db)} players.")