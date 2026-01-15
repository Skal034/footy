import random
import csv
import configparser
from faker import Faker
from deep_translator import GoogleTranslator
import geography as geo # Importing the geography module to access locales
import player as p

# Build Faker factories from the locale definitions
fake_factory = {nation: Faker(info['locale']) for nation, info in geo.locales.items()}

# Helper: numeric FIFA points for each locale (extracted from locales)
fifa_points = {nation: info.get('fifa') for nation, info in geo.locales.items()}

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
        if country in ["Spain", 'Mexico', 'Argentina', 'Colombia']:
            prefixes = ["Real", "Atlético", "Deportivo"]
            name = f"{random.choice(prefixes)} {city}" if random.random() > 0.4 else f"{city} CF"
        elif country in ["England", "Ireland", "Scotland", "USA"] and random.random() > 0.7:
            suffixes = ["United", "City", "Town", "Rovers", "Athletic", "FC"]
            name = f"{city} {random.choice(suffixes)}"
        else:
            name = f"{city} {fk.last_name()}s" 
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
        #if self.locale in ("ja_JP", "ko_KR", "zh_CN", "bn_BD", "ar_DZ", "ar_SA", 
        #                   "ru_RU", "ka_GE", "he_IL", "hy_AM", "el_GR", "fa_IR",
        #                   "uk_UA"):
        self.name = GoogleTranslator(source='auto', target='en').translate(self.name)
        
        self.age = random.randint(AGE_MIN, AGE_MAX)
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
        self.stats = {attr: 0 for attr in p.ALL_ATTRIBUTES}
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
            return country, geo.locales.get(country, {}).get('locale', 'en_GB')

        nations = list(geo.locales.keys())
        # base multiplier: teams with higher base_rating slightly favour top nations
        base_mult = 1.0 + ((base_rating - 60) / 100.0)
        weights = [max(1.0, fifa_points.get(n) * base_mult) for n in nations]
        total = sum(weights)
        # normalized selection
        r = random.random() * total
        upto = 0.0
        for n, w in zip(nations, weights):
            upto += w
            if r <= upto:
                return n, geo.locales.get(n, {}).get('locale', 'en_GB')
        last = nations[-1]
        return last, geo.locales.get(last, {}).get('locale', 'en_GB')

    def _generate_stats(self):
        """Assigns ratings based on whether the player is a GK or Outfield player."""
        base = self.overall
        if self.position == "GK":
            for s in ["Reflexes", "Positioning", "Handling", "Distribution", "Sweeping"]:
                self.stats[s] = max(1, min(99, base + random.randint(-5, 10)))
        else:
            # Outfield stats are index 5 onwards in the ALL_ATTRIBUTES list
            for s in p.ALL_ATTRIBUTES[5:]:
                self.stats[s] = max(1, min(99, base + random.randint(-8, 8)))
            
            # Positional bias logic
            cat = p.POS_MAP[self.position]
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
            cat = p.POS_MAP[p.position]
            assigned = False
            for num in p.SHIRT_PREFS[cat]:
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
    config = configparser.ConfigParser()
    config.read('config.ini')
    AGE_MIN = config.getint('Players_Config', 'AGE_MIN', fallback=16)
    AGE_MAX = config.getint('Players_Config', 'AGE_MAX', fallback=40)

    for l_id, conf in geo.LEAGUES.items():
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