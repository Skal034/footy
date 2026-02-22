# --- 1. LOCALIZED FACTORY SETUP ---
# Locales for Player names and Team cities

#country ratings source: https://www.sofascore.com/football/rankings/fifa
#locale: faker_locale
#rating: fifa ranking points
locales = {
    
    ##Europe
    'England': {'locale': 'en_GB', 'rating': 1834.12}, 'Italy': {'locale': 'it_IT', 'rating': 1702.06},
    'Netherlands': {'locale': 'nl_NL', 'rating': 1756.27}, 'Spain': {'locale': 'es_ES', 'rating': 1877.18},
    'France': {'locale': 'fr_FR', 'rating': 1870.00}, 'Germany': {'locale': 'de_DE', 'rating': 1724.15},
    'Portugal': {'locale': 'pt_PT', 'rating': 1760.38}, 'Austria': {'locale': 'de_AT', 'rating': 1585.12},
    'Belgium': {'locale': 'fr_BE', 'rating': 1730.71}, 'Estonia': {'locale': 'et_EE', 'rating': 1123.11},
    'Sweden': {'locale': 'sv_SE', 'rating': 1487.13}, 'Norway': {'locale': 'no_NO', 'rating': 1553.14},
    'Denmark': {'locale': 'da_DK', 'rating': 1616.75}, 'Finland': {'locale': 'fi_FI', 'rating': 1341.81},
    'Russia': {'locale': 'ru_RU', 'rating': 1524.52}, 'Ukraine': {'locale': 'uk_UA', 'rating': 1557.47},
    'Poland': {'locale': 'pl_PL', 'rating': 1532.04}, 'Czechia': {'locale': 'cs_CZ', 'rating': 1487.00},
    'Slovakia': {'locale': 'sk_SK', 'rating': 1485.65}, 'Hungary': {'locale': 'hu_HU', 'rating': 1496.29},
    'Romania': {'locale': 'ro_RO', 'rating': 1465.78}, 'Bulgaria': {'locale': 'ro_RO', 'rating': 1272.19},
    'Greece': {'locale': 'el_GR', 'rating': 1480.38}, 'Turkey': {'locale': 'tr_TR', 'rating': 1582.69},
    'Belarus': {'locale': 'ru_RU', 'rating': 1227.09}, 'Serbia': {'locale': 'hr_HR', 'rating': 1506.34},
    'Croatia': {'locale': 'hr_HR', 'rating': 1716.88}, 'Slovenia': {'locale': 'sl_SI', 'rating': 1447.31},
    'Bosnia and Herzegovina': {'locale': 'hu_HU', 'rating': 1362.37}, 'North Macedonia': {'locale': 'hr_HR', 'rating': 1378.57},
    'Albania': {'locale': 'hu_HU', 'rating': 1401.07}, 'Montenegro': {'locale': 'hr_HR', 'rating': 1297.09},
    'Iceland': {'locale': 'is_IS', 'rating': 1344.72}, 'Luxembourg': {'locale': 'fr_FR', 'rating': 1218.91},
    'Malta': {'locale': 'el_GR', 'rating': 996.59}, 'Cyprus': {'locale': 'el_GR', 'rating': 1128.50},
    'Azerbaijan': {'locale': 'az_AZ', 'rating': 1132.97}, 'Georgia': {'locale': 'ka_GE', 'rating': 1347.88},
    'Armenia': {'locale': 'hy_AM', 'rating': 1196.08}, 'Latvia': {'locale': 'lv_LV', 'rating': 1082.68},
    'Lithuania': {'locale': 'lt_LT', 'rating': 1056.34}, 'Switzerland': {'locale': 'fr_CH', 'rating': 1654.69},
    'Scotland': {'locale': 'en_GB', 'rating': 1506.77}, 'Wales': {'locale': 'en_GB', 'rating': 1529.71},
    'Northern Ireland': {'locale': 'ga_IE', 'rating': 1366.02}, 'Ireland': {'locale': 'ga_IE', 'rating': 1580.12},
    'Kosovo': {'locale': 'hr_HR', 'rating': 1308.84},

    ##North America
    'USA': {'locale': 'en_US', 'rating': 1681.88}, 'Bahamas': {'locale': 'en_US', 'rating': 796.60},
    'Saint Lucia': {'locale': 'en_US', 'rating': 980.28}, 'Grenada': {'locale': 'en_US', 'rating': 989.59},
    'Antigua and Barbuda': {'locale': 'en_US', 'rating': 986.58}, 'Saint Kitts and Nevis': {'locale': 'en_US', 'rating': 1035.25},
    'Barbados': {'locale': 'en_US', 'rating': 914.42}, 'Canada': {'locale': 'en_CA', 'rating': 1559.15},
    'Mexico': {'locale': 'es_MX', 'rating': 1675.75}, 'Costa Rica': {'locale': 'es_CL', 'rating': 1464.24},
    'Panama': {'locale': 'es_ES', 'rating': 1540.43}, 'Honduras': {'locale': 'es_ES', 'rating': 1379.54},
    'Guatemala': {'locale': 'es_ES', 'rating': 1245.77}, 'El Salvador': {'locale': 'es_ES', 'rating': 1226.65},
    'Nicaragua': {'locale': 'es_ES', 'rating': 1116.86}, 'Dominican Republic': {'locale': 'es_ES', 'rating': 1077.49},
    'Cuba': {'locale': 'es_ES', 'rating': 980.49}, 'Jamaica': {'locale': 'en_US', 'rating': 1362.46},
    'Trinidad and Tobago': {'locale': 'en_US', 'rating': 1227.32}, 'Haiti': {'locale': 'fr_FR', 'rating': 1294.49},
    'Curacao': {'locale': 'es_ES', 'rating': 1302.7},
    
    ##South America
    'Brazil': {'locale': 'pt_BR', 'rating': 1760.46}, 'Venezuela': {'locale': 'es_CL', 'rating': 1465.22}, 
    'Argentina': {'locale': 'es_AR', 'rating': 1873.33}, 'Colombia': {'locale': 'es_CL', 'rating': 1701.30},
    'Chile': {'locale': 'es_CL', 'rating': 1457.84}, 'Peru': {'locale': 'es_CL', 'rating': 1459.57},
    'Uruguay': {'locale': 'es_AR', 'rating': 1672.62}, 'Paraguay': {'locale': 'es_ES', 'rating': 1501.50},
    'Bolivia': {'locale': 'es_CL', 'rating': 1329.56}, 'Ecuador': {'locale': 'es_CL', 'rating': 1591.73},

    ##Africa
    'South Africa': {'locale': 'yo_NG', 'rating': 1426.73}, 'Nigeria': {'locale': 'ig_NG', 'rating': 1502.46},
    'Ghana': {'locale': 'tw_GH', 'rating': 1351.09}, 'Cameroon': {'locale': 'en_NG', 'rating': 1440.43},
    'Senegal': {'locale': 'en_NG', 'rating': 1648.07}, 'Ivory Coast': {'locale': 'en_NG', 'rating': 1489.59},
    'DR Congo': {'locale': 'en_NG', 'rating': 1444.16}, 'Equatorial Guinea': {'locale': 'yo_NG', 'rating': 1229.09},
    'Ethiopia': {'locale': 'ig_NG', 'rating': 1055.36}, 'Kenya': {'locale': 'en_KE', 'rating': 1179.54},
    'Uganda': {'locale': 'ig_NG', 'rating': 1288.01}, 'Zambia': {'locale': 'ig_NG', 'rating': 1258.4},
    'Zimbabwe': {'locale': 'yo_NG', 'rating': 1123.69}, 'Tanzania': {'locale': 'ig_NG', 'rating': 1181.22},
    'Egypt': {'locale': 'ar_SA', 'rating': 1515.18}, 'Morocco': {'locale': 'ar_DZ', 'rating': 1716.34},
    'Algeria': {'locale': 'ar_DZ', 'rating': 1517.68}, 'Tunisia': {'locale': 'ar_DZ', 'rating': 1494.86},
    'Mali' : {'locale': 'yo_NG', 'rating': 1455.03}, 'Burkina Faso': {'locale': 'yo_NG', 'rating': 1404.81},
    'Cape Verde': {'locale': 'fr_FR', 'rating': 1370.49}, 'Gabon': {'locale': 'yo_NG', 'rating': 1321.25},
    'Angola': {'locale': 'yo_NG', 'rating': 1271.54}, 'Guinea': {'locale': 'yo_NG', 'rating': 1307.05},
    'Benin': {'locale': 'yo_NG', 'rating': 1255.72}, 'Niger': {'locale': 'yo_NG', 'rating': 1185.09},
    'Libya': {'locale': 'ar_DZ', 'rating': 1183.06}, 'Mozambique': {'locale': 'yo_NG', 'rating': 1223.48},
    
    ##Oceania
    'Australia': {'locale': 'en_AU', 'rating': 1574.01}, 'Fiji': {'locale': 'en_AU', 'rating': 1029.7}, 
    'New Zealand': {'locale': 'en_NZ', 'rating': 1279.25}, 'Solomon Islands': {'locale': 'en_AU', 'rating': 1039.86},

    ##Asia    
    'Japan': {'locale': 'ja_JP', 'rating': 1650.12}, 'South Korea': {'locale': 'ko_KR', 'rating': 1599.45},
    'China': {'locale': 'zh_CN', 'rating': 1249.06}, 'India': {'locale': 'en_IN', 'rating': 1079.52},
    'Vietnam': {'locale': 'vi_VN', 'rating': 1189.51}, 'Thailand': {'locale': 'en_TH', 'rating': 1243.27},
    'Indonesia': {'locale': 'id_ID', 'rating': 1144.73}, 'Malaysia': {'locale': 'id_ID', 'rating': 1145.89},
    'Philippines': {'locale': 'id_ID', 'rating': 1090.95}, 'Bangladesh': {'locale': 'bn_BD', 'rating': 911.1},
    'Pakistan': {'locale': 'en_PK', 'rating': 833.16},  'Syria': {'locale': 'ar_SA', 'rating': 1282.62},
    'Israel': {'locale': 'he_IL', 'rating': 1328.14}, 'Palestine': {'locale': 'ar_DZ', 'rating': 1244.73},
    'Saudi Arabia': {'locale': 'ar_SA', 'rating': 1429.48}, 'UAE': {'locale': 'ar_DZ', 'rating': 1370.47},
    'Qatar': {'locale': 'ar_DZ', 'rating': 1454.96}, 'Kuwait': {'locale': 'ar_DZ', 'rating': 1105.10},
    'Bahrain': {'locale': 'ar_DZ', 'rating': 1258.53}, 'Oman': {'locale': 'ar_DZ', 'rating': 1313.46},
    'Jordan': {'locale': 'ar_DZ', 'rating': 1388.93}, 'Lebanon': {'locale': 'ar_SA', 'rating': 1187.96},
    'Iraq': {'locale': 'ar_SA', 'rating': 1436.94}, 'Iran': {'locale': 'fa_IR', 'rating': 1617.02},
    'Kazakhstan': {'locale': 'uz_UZ', 'rating': 1173.0}, 'Tajikistan': {'locale': 'uz_UZ', 'rating': 1224.93},
    'Uzbekistan': {'locale': 'uz_UZ', 'rating': 1462.03}, 'Kyrgyzstan': {'locale': 'uz_UZ', 'rating': 1201.22},
    
}

#names from these locales need to be transliterated to Latin script 
locales_to_be_romanized = {
    "ja_JP", "ko_KR", "zh_CN", "bn_BD", "ar_DZ", "ar_SA", "ru_RU", "fa_IR", 
    "he_IL", "el_GR", "ka_GE", "hy_AM", "uk_UA"}

# --- 2. LEAGUES CONFIGURATION ---

#league ratings source : https://theanalyst.com/articles/strongest-football-leagues-in-the-world-opta-power-rankings
#ratings = league strength, 
#teams = #of teams in the league, 
#local_weight = fraction of local players (vs foreigners)
LEAGUES = {
    #europe
    "ENG_1": {"name": "Premier League", "country": "England", "rating": 92.7, "teams": 20, "local_weight": 0.4},
    "ENG_2": {"name": "Championship", "country": "England", "rating": 83.0, "teams": 24, "local_weight": 0.65},
    "ESP_1": {"name": "La Liga", "country": "Spain", "rating": 86.3, "teams": 20, "local_weight": 0.48},
    "ESP_2": {"name": "La Liga 2", "country": "Spain", "rating": 78.6, "teams": 22, "local_weight": 0.7},
    "FRA_1": {"name": "Ligue 1", "country": "France", "rating": 85.2, "teams": 20, "local_weight": 0.5},
    "FRA_2": {"name": "Ligue 2", "country": "France", "rating": 76.7, "teams": 20, "local_weight": 0.7},
    "GER_1": {"name": "Bundesliga", "country": "Germany", "rating": 86.7, "teams": 18, "local_weight": 0.45},
    "GER_2": {"name": "2. Bundesliga", "country": "Germany", "rating": 79.0, "teams": 18, "local_weight": 0.68},
    "ITA_1": {"name": "Serie A", "country": "Italy", "rating": 86.4, "teams": 20, "local_weight": 0.5},
    "ITA_2": {"name": "Serie B", "country": "Italy", "rating": 77.6, "teams": 20, "local_weight": 0.75},
    "POR_1": {"name": "Primeira Liga", "country": "Portugal", "rating": 82.0, "teams": 18, "local_weight": 0.65},
    "POR_2": {"name": "Segunda Liga", "country": "Portugal", "rating": 74.4, "teams": 20, "local_weight": 0.8},
    "NLD_1": {"name": "Eredivisie", "country": "Netherlands", "rating": 79.0, "teams": 18, "local_weight": 0.7},
    "BEL_1": {"name": "Jupiler Pro League", "country": "Belgium", "rating": 82.8, "teams": 16, "local_weight": 0.8},
    "DEN_1": {"name": "Superliga", "country": "Denmark", "rating": 81.0, "teams": 16, "local_weight": 0.75},
    "NOR_1": {"name": "Eliteserien", "country": "Norway", "rating": 79.1, "teams": 16, "local_weight": 0.8},
    "SWE_1": {"name": "Allsvenskan", "country": "Sweden", "rating": 77.6, "teams": 16, "local_weight": 0.8},
    "SCO_1": {"name": "Scottish Premiership", "country": "Scotland", "rating": 76.9, "teams": 14, "local_weight": 0.65},
    "IRE_1": {"name": "Irish League", "country": "Ireland", "rating": 72.1, "teams": 14, "local_weight": 0.87},
    "POL_1": {"name": "Polish Ekstraklasa", "country": "Poland", "rating": 80.4, "teams": 20, "local_weight": 0.78},
    "CZE_1": {"name": "Czech First League", "country": "Czechia", "rating": 78.7, "teams": 16, "local_weight": 0.75},
    "RUS_1": {"name": "Russian Premier League", "country": "Russia", "rating": 78.5, "teams": 18, "local_weight": 0.75},
    "TUR_1": {"name": "Turkish Süper Lig", "country": "Turkey", "rating": 79.3, "teams": 18, "local_weight": 0.70},
    "SUI_1": {"name": "Swiss Super League", "country": "Switzerland", "rating": 78.8, "teams": 10, "local_weight": 0.71},
    "AUT_1": {"name": "Austrian Bundesliga", "country": "Austria", "rating": 77.5, "teams": 12, "local_weight": 0.76},
    

    #north america
    "USA_1": {"name": "MLS", "country": "USA", "rating": 80.3, "teams": 18, "local_weight": 0.50},
    "MEX_1": {"name": "Liga MX", "country": "Mexico", "rating": 78.3, "teams": 18, "local_weight": 0.68},

    #south america
    "ARG_1": {"name": "Liga Profesional Argentina", "country": "Argentina", "rating": 82.0, "teams": 20, "local_weight": 0.8},
    "BRA_1": {"name": "Brazilian Serie A", "country": "Brazil", "rating": 81.8, "teams": 20, "local_weight": 0.8},
    "BRA_2": {"name": "Brazilian Serie B", "country": "Brazil", "rating": 71.2, "teams": 20, "local_weight": 0.92},
    "CHL_1": {"name": "Chilean League", "country": "Chile", "rating": 77.4, "teams": 20, "local_weight": 0.86},
    "COL_1": {"name": "Colombian League", "country": "Colombia", "rating": 79.9, "teams": 20, "local_weight": 0.83},

    #asia and oceania
    "IND_1": {"name": "Indian Super League", "country": "India", "rating": 64.0, "teams": 12, "local_weight": 0.9},
    "AUS_1": {"name": "A-League", "country": "Australia", "rating": 73.2, "teams": 10, "local_weight": 0.89},
    "JPN_1": {"name": "J. League", "country": "Japan", "rating": 79.2, "teams": 18, "local_weight": 0.91},
    "KOR_1": {"name": "K League 1", "country": "South Korea", "rating": 75.9, "teams": 12, "local_weight": 0.95},
    "SAU_1": {"name": "Saudi Professional League", "country": "Saudi Arabia", "rating": 77.1, "teams": 16, "local_weight": 0.65},
}

import random
from faker import Faker
import player as p
import config_reader as cfg

# Build Faker factories from the locale definitions
fake_factory = {nation: Faker(info['locale']) for nation, info in locales.items()}

# Helper: numeric FIFA points for each locale (extracted from locales)
rating_points = {nation: info.get('rating') for nation, info in locales.items()}

# Normalized locales from 40 to 100
min_rating = min(rating_points.values())
max_rating = max(rating_points.values())
normalized_locales = {
    nation: {
        **locales[nation],
        'normalized_rating': 40 + (rating_points[nation] - min_rating) / (max_rating - min_rating) * 60
    }
    for nation in locales.keys()
}

class Team:
    def __init__(self, name, league_config, team_rating):
        self.name = name
        league_rating = league_config['rating']
        #team rating is capped to 95
        strength_variance = cfg.TEAM_STRENGTH_VARIANCE
        self.base_ovr = min(95,random.gauss(league_rating + 3*strength_variance*team_rating, strength_variance))
        
        # 30 players per squad
        player_variance = cfg.PLAYER_STRENGTH_VARIANCE
        self.players = [p.Player(self.name, league_config, self.base_ovr + random.randint(-1*player_variance, player_variance)) for _ in range(30)]
        self._assign_jerseys()

    def _assign_jerseys(self):
        """Star players get priority for iconic numbers; no duplicates allowed."""
        used = set()
        # High-rated players pick first
        for plr in sorted(self.players, key=lambda x: x.overall, reverse=True):
            cat = p.POS_MAP[plr.position]
            assigned = False
            for num in p.SHIRT_PREFS[cat]:
                if num not in used:
                    plr.jersey = num
                    used.add(num)
                    assigned = True
                    break
            
            if not assigned:
                while True:
                    rand_num = random.randint(1, 40) # Kit numbers allowed up to 40
                    if rand_num not in used:
                        plr.jersey = rand_num
                        used.add(rand_num)
                        break


# --- League and Team name generation for leagues ---
def generate_league_team_names(country, count):
    """Generates unique team names based on country geography and local naming styles."""
    names = set()
    fk = fake_factory.get(country, fake_factory['England'])

    cities = []
    while len(set(cities)) < count:
        city_name = p.translate_to_en(fk.city()) if fk.locale in locales_to_be_romanized else fk.city()
        cities.append(city_name)
    # preserve order while deduplicating
    cities = list(dict.fromkeys(cities))

    for city in cities:
        name = None

        # Czechia
        if country == "Czechia":
            name = f"{city} {random.choice(['FK','SK','AC','FC'])}"

        # Poland
        elif country == "Poland":
            if random.random() > 0.5:
                name = f"{random.choice(['KS','Górnik','Lech','Legia'])} {city}"
            else:
                name = f"{city} {random.choice(['FC','KS'])}"

        # Scotland
        elif country == "Scotland":
            suffixes = ["United", "City", "Town", "Rovers", "Athletic", "FC", "RFC"]
            name = f"{city} {random.choice(suffixes)}"

        # Ireland
        elif country == "Ireland":
            suffixes = ["United", "Rovers", "Athletic", "FC", "AFC"]
            name = f"{city} {random.choice(suffixes)}"

        # India
        elif country == "India":
            patterns = [f"{city} FC", f"{city} City", f"{city} United", f"{city} Blasters", f"{fk.last_name()} FC"]
            name = random.choice(patterns)

        # South Korea
        elif country == "South Korea":
            name = f"{city} {random.choice(['FC','SC','United'])}"

        # Colombia (handle common misspelling 'Columbia' as well)
        elif country in ["Colombia", "Columbia"]:
            prefixes = ["Atlético", "Deportivo", "Independiente", "Club"]
            name = f"{random.choice(prefixes)} {city}" if random.random() > 0.4 else f"{city} FC"

        # Chile
        elif country == "Chile":
            prefixes = ["Universidad", "Colo-Colo", "Deportivo", "Club"]
            name = f"{random.choice(prefixes)} {city}" if random.random() > 0.4 else f"{city} FC"

        # Iberian / Latin patterns (Spain, Mexico, Argentina and others)
        elif country in ["Spain", 'Mexico', 'Argentina']:
            prefixes = ["Real", "Atlético", "Deportivo"]
            name = f"{random.choice(prefixes)} {city}" if random.random() > 0.4 else f"{city} CF"

        # Germany: common prefixes/suffixes like FC, SV, SC, VfL, Borussia
        elif country == "Germany":
            if random.random() > 0.6:
                name = f"{random.choice(['Borussia','VfL','TSV'])} {fk.last_name()}"
            else:
                name = f"{city} {random.choice(['FC','SV','SC'])}"

        # Italy: AC, AS, Calcio, common "Calcio" and small-club patterns
        elif country == "Italy":
            patterns = [f"AC {city}", f"{city} Calcio", f"{city} FC", f"AS {fk.last_name()}"]
            name = random.choice(patterns)

        # Austria: FK, SV, SC or 'Austria {city}'
        elif country == "Austria":
            if random.random() > 0.5:
                name = f"{random.choice(['FK','SV','SC','Austria'])} {city}"
            else:
                name = f"{city} {random.choice(['FC','SC'])}"

        # Brazil: Esporte Clube, Clube, Atlético, {city} FC
        elif country == "Brazil":
            patterns = [f"Esporte Clube {city}", f"{city} EC", f"Clube {city}", f"Atlético {city}", f"{city} FC"]
            name = random.choice(patterns)

        # Portugal: Sporting/Benfica style or simple 'FC {city}'
        elif country == "Portugal":
            patterns = [f"Sporting {city}", f"Benfica {fk.last_name()}", f"FC {city}", f"{city} SC"]
            name = random.choice(patterns)

        # Denmark: Boldklubben (BK), IF, FC
        elif country == "Denmark":
            name = f"{city} {random.choice(['BK','IF','FC','Boldklubben'])}"

        # Sweden: IF, IK, BK, FF suffixes
        elif country == "Sweden":
            name = f"{city} {random.choice(['IF','IK','BK','FF'])}"

        # France: Olympique, Stade, AS or simple FC
        elif country == "France":
            if random.random() > 0.4:
                name = f"{random.choice(['Olympique','Stade','AS'])} {city}"
            else:
                name = f"{city} FC"

        # Belgium: Koninklijke/KV/KRC/Racing prefixes
        elif country == "Belgium":
            if random.random() > 0.5:
                name = f"{random.choice(['KV','KRC','Royal','Racing'])} {city}"
            else:
                name = f"{city} {random.choice(['FC','KV'])}"

        # Australia: A-League patterns like 'FC', 'United', 'Wanderers', 'Mariners'
        elif country == "Australia":
            name = f"{city} {random.choice(['FC','United','Wanderers','Mariners','City'])}"

        # Japan: J.League clubs often use 'FC', 'SC' or unique nicknames; keep plausible options
        elif country == "Japan":
            if random.random() > 0.6:
                name = f"{city} {random.choice(['FC','SC'])}"
            else:
                name = f"{fk.last_name()} {random.choice(['Antlers','Frontale','Sanga','Grampus'])}"

        # Saudi Arabia / Gulf: many clubs start with 'Al' (Al-Hilal, Al-Nassr...)
        elif country in ["Saudi Arabia", "UAE", "Qatar", "Kuwait"]:
            if random.random() > 0.6:
                name = f"Al {fk.last_name()}"
            else:
                # hyphenated city form is also common in transliterations
                name = f"Al-{city}"

        # Netherlands: common 'FC' or 'VV' styling
        elif country == "Netherlands":
            name = f"{city} {random.choice(['FC','VV','SC'])}"

        # Turkey: many clubs use 'SK' or unique names; provide 'SK' and some famous-sounding prefixes
        elif country == "Turkey":
            if random.random() > 0.8:
                name = f"{random.choice(['Beşiktaş','Galatasaray','Fenerbahçe'])} {fk.last_name()}"
            else:
                name = f"{city} SK"

        # Switzerland and similar: FC/SC or historical names
        elif country == "Switzerland":
            name = f"{city} {random.choice(['FC','SC','Grasshoppers'])}"

        # Fallbacks: English-style or last-name-based club
        else:
            if country in ["England", "Ireland", "Scotland", "USA"] and random.random() > 0.7:
                suffixes = ["United", "City", "Town", "Rovers", "Athletic", "FC"]
                name = f"{city} {random.choice(suffixes)}"
            else:
                name = f"{city} {fk.last_name()}s"

        names.add(name)

    return list(names)[:count]