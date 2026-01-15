# --- 1. LOCALIZED FACTORY SETUP ---
# Locales for Player names and Team cities
locales = {
    # Core footballing countries (kept original keys for compatibility)
    # Each entry: { 'locale': <faker_locale>, 'fifa': <points> }

    ##Europe
    'England': {'locale': 'en_GB', 'fifa': 1834.12}, 'Italy': {'locale': 'it_IT', 'fifa': 1702.06},
    'Netherlands': {'locale': 'nl_NL', 'fifa': 1756.27}, 'Spain': {'locale': 'es_ES', 'fifa': 1877.18},
    'France': {'locale': 'fr_FR', 'fifa': 1870.00}, 'Germany': {'locale': 'de_DE', 'fifa': 1724.15},
    'Portugal': {'locale': 'pt_PT', 'fifa': 1760.38}, 'Austria': {'locale': 'de_AT', 'fifa': 1585.12},
    'Belgium': {'locale': 'fr_BE', 'fifa': 1730.71}, 'Estonia': {'locale': 'et_EE', 'fifa': 1123.11},
    'Sweden': {'locale': 'sv_SE', 'fifa': 1487.13}, 'Norway': {'locale': 'no_NO', 'fifa': 1553.14},
    'Denmark': {'locale': 'da_DK', 'fifa': 1616.75}, 'Finland': {'locale': 'fi_FI', 'fifa': 1341.81},
    'Russia': {'locale': 'ru_RU', 'fifa': 1524.52}, 'Ukraine': {'locale': 'uk_UA', 'fifa': 1557.47},
    'Poland': {'locale': 'pl_PL', 'fifa': 1532.04}, 'Czechia': {'locale': 'cs_CZ', 'fifa': 1487.00},
    'Slovakia': {'locale': 'sk_SK', 'fifa': 1485.65}, 'Hungary': {'locale': 'hu_HU', 'fifa': 1496.29},
    'Romania': {'locale': 'ro_RO', 'fifa': 1465.78}, 'Bulgaria': {'locale': 'ro_RO', 'fifa': 1272.19},
    'Greece': {'locale': 'el_GR', 'fifa': 1480.38}, 'Turkey': {'locale': 'tr_TR', 'fifa': 1582.69},
    'Belarus': {'locale': 'ru_RU', 'fifa': 1227.09}, 'Serbia': {'locale': 'hr_HR', 'fifa': 1506.34},
    'Croatia': {'locale': 'hr_HR', 'fifa': 1716.88}, 'Slovenia': {'locale': 'sl_SI', 'fifa': 1447.31},
    'Bosnia and Herzegovina': {'locale': 'hu_HU', 'fifa': 1362.37}, 'North Macedonia': {'locale': 'hr_HR', 'fifa': 1378.57},
    'Albania': {'locale': 'hu_HU', 'fifa': 1401.07}, 'Montenegro': {'locale': 'hr_HR', 'fifa': 1297.09},
    'Iceland': {'locale': 'is_IS', 'fifa': 1344.72}, 'Luxembourg': {'locale': 'fr_FR', 'fifa': 1218.91},
    'Malta': {'locale': 'el_GR', 'fifa': 996.59}, 'Cyprus': {'locale': 'el_GR', 'fifa': 1128.50},
    'Azerbaijan': {'locale': 'az_AZ', 'fifa': 1132.97}, 'Georgia': {'locale': 'ka_GE', 'fifa': 1347.88},
    'Armenia': {'locale': 'hy_AM', 'fifa': 1196.08}, 'Latvia': {'locale': 'lv_LV', 'fifa': 1082.68},
    'Lithuania': {'locale': 'lt_LT', 'fifa': 1056.34}, 'Switzerland': {'locale': 'fr_CH', 'fifa': 1654.69},
    'Scotland': {'locale': 'en_GB', 'fifa': 1506.77}, 'Wales': {'locale': 'en_GB', 'fifa': 1529.71},
    'Northern Ireland': {'locale': 'ga_IE', 'fifa': 1366.02}, 'Ireland': {'locale': 'ga_IE', 'fifa': 1580.12},
    'Kosovo': {'locale': 'hr_HR', 'fifa': 1308.84},

    ##North America
    'USA': {'locale': 'en_US', 'fifa': 1681.88}, 'Bahamas': {'locale': 'en_US', 'fifa': 796.60},
    'Saint Lucia': {'locale': 'en_US', 'fifa': 980.28}, 'Grenada': {'locale': 'en_US', 'fifa': 989.59},
    'Antigua and Barbuda': {'locale': 'en_US', 'fifa': 986.58}, 'Saint Kitts and Nevis': {'locale': 'en_US', 'fifa': 1035.25},
    'Barbados': {'locale': 'en_US', 'fifa': 914.42}, 'Canada': {'locale': 'en_CA', 'fifa': 1559.15},
    'Mexico': {'locale': 'es_MX', 'fifa': 1675.75}, 'Costa Rica': {'locale': 'es_CL', 'fifa': 1464.24},
    'Panama': {'locale': 'es_ES', 'fifa': 1540.43}, 'Honduras': {'locale': 'es_ES', 'fifa': 1379.54},
    'Guatemala': {'locale': 'es_ES', 'fifa': 1245.77}, 'El Salvador': {'locale': 'es_ES', 'fifa': 1226.65},
    'Nicaragua': {'locale': 'es_ES', 'fifa': 1116.86}, 'Dominican Republic': {'locale': 'es_ES', 'fifa': 1077.49},
    'Cuba': {'locale': 'es_ES', 'fifa': 980.49}, 'Jamaica': {'locale': 'en_US', 'fifa': 1362.46},
    'Trinidad and Tobago': {'locale': 'en_US', 'fifa': 1227.32}, 'Haiti': {'locale': 'fr_FR', 'fifa': 1294.49},
    'Curacao': {'locale': 'es_ES', 'fifa': 1302.7},
    
    ##South America
    'Brazil': {'locale': 'pt_BR', 'fifa': 1760.46}, 'Venezuela': {'locale': 'es_CL', 'fifa': 1465.22}, 
    'Argentina': {'locale': 'es_AR', 'fifa': 1873.33}, 'Colombia': {'locale': 'es_CL', 'fifa': 1701.30},
    'Chile': {'locale': 'es_CL', 'fifa': 1457.84}, 'Peru': {'locale': 'es_CL', 'fifa': 1459.57},
    'Uruguay': {'locale': 'es_AR', 'fifa': 1672.62}, 'Paraguay': {'locale': 'es_ES', 'fifa': 1501.50},
    'Bolivia': {'locale': 'es_CL', 'fifa': 1329.56}, 'Ecuador': {'locale': 'es_CL', 'fifa': 1591.73},

    ##Africa
    'South Africa': {'locale': 'yo_NG', 'fifa': 1426.73}, 'Nigeria': {'locale': 'ig_NG', 'fifa': 1502.46},
    'Ghana': {'locale': 'tw_GH', 'fifa': 1351.09}, 'Cameroon': {'locale': 'en_NG', 'fifa': 1440.43},
    'Senegal': {'locale': 'en_NG', 'fifa': 1648.07}, 'Ivory Coast': {'locale': 'en_NG', 'fifa': 1489.59},
    'DR Congo': {'locale': 'en_NG', 'fifa': 1444.16}, 'Equatorial Guinea': {'locale': 'yo_NG', 'fifa': 1229.09},
    'Ethiopia': {'locale': 'ig_NG', 'fifa': 1055.36}, 'Kenya': {'locale': 'en_KE', 'fifa': 1179.54},
    'Uganda': {'locale': 'ig_NG', 'fifa': 1288.01}, 'Zambia': {'locale': 'ig_NG', 'fifa': 1258.4},
    'Zimbabwe': {'locale': 'yo_NG', 'fifa': 1123.69}, 'Tanzania': {'locale': 'ig_NG', 'fifa': 1181.22},
    'Egypt': {'locale': 'ar_SA', 'fifa': 1515.18}, 'Morocco': {'locale': 'ar_DZ', 'fifa': 1716.34},
    'Algeria': {'locale': 'ar_DZ', 'fifa': 1517.68}, 'Tunisia': {'locale': 'ar_DZ', 'fifa': 1494.86},
    'Mali' : {'locale': 'yo_NG', 'fifa': 1455.03}, 'Burkina Faso': {'locale': 'yo_NG', 'fifa': 1404.81},
    'Cape Verde': {'locale': 'fr_FR', 'fifa': 1370.49}, 'Gabon': {'locale': 'yo_NG', 'fifa': 1321.25},
    'Angola': {'locale': 'yo_NG', 'fifa': 1271.54}, 'Guinea': {'locale': 'yo_NG', 'fifa': 1307.05},
    'Benin': {'locale': 'yo_NG', 'fifa': 1255.72}, 'Niger': {'locale': 'yo_NG', 'fifa': 1185.09},
    'Libya': {'locale': 'ar_DZ', 'fifa': 1183.06}, 'Mozambique': {'locale': 'yo_NG', 'fifa': 1223.48},
    
    ##Oceania
    'Australia': {'locale': 'en_AU', 'fifa': 1574.01}, 'Fiji': {'locale': 'en_AU', 'fifa': 1029.7}, 
    'New Zealand': {'locale': 'en_NZ', 'fifa': 1279.25}, 'Solomon Islands': {'locale': 'en_AU', 'fifa': 1039.86},

    ##Asia    
    'Japan': {'locale': 'ja_JP', 'fifa': 1650.12}, 'South Korea': {'locale': 'ko_KR', 'fifa': 1599.45},
    'China': {'locale': 'zh_CN', 'fifa': 1249.06}, 'India': {'locale': 'en_IN', 'fifa': 1079.52},
    'Vietnam': {'locale': 'vi_VN', 'fifa': 1189.51}, 'Thailand': {'locale': 'en_TH', 'fifa': 1243.27},
    'Indonesia': {'locale': 'id_ID', 'fifa': 1144.73}, 'Malaysia': {'locale': 'id_ID', 'fifa': 1145.89},
    'Philippines': {'locale': 'id_ID', 'fifa': 1090.95}, 'Bangladesh': {'locale': 'bn_BD', 'fifa': 911.1},
    'Pakistan': {'locale': 'en_PK', 'fifa': 833.16},  'Syria': {'locale': 'ar_SA', 'fifa': 1282.62},
    'Israel': {'locale': 'he_IL', 'fifa': 1328.14}, 'Palestine': {'locale': 'ar_DZ', 'fifa': 1244.73},
    'Saudi Arabia': {'locale': 'ar_SA', 'fifa': 1429.48}, 'UAE': {'locale': 'ar_DZ', 'fifa': 1370.47},
    'Qatar': {'locale': 'ar_DZ', 'fifa': 1454.96}, 'Kuwait': {'locale': 'ar_DZ', 'fifa': 1105.10},
    'Bahrain': {'locale': 'ar_DZ', 'fifa': 1258.53}, 'Oman': {'locale': 'ar_DZ', 'fifa': 1313.46},
    'Jordan': {'locale': 'ar_DZ', 'fifa': 1388.93}, 'Lebanon': {'locale': 'ar_SA', 'fifa': 1187.96},
    'Iraq': {'locale': 'ar_SA', 'fifa': 1436.94}, 'Iran': {'locale': 'fa_IR', 'fifa': 1617.02},
    'Kazakhstan': {'locale': 'uz_UZ', 'fifa': 1173.0}, 'Tajikistan': {'locale': 'uz_UZ', 'fifa': 1224.93},
    'Uzbekistan': {'locale': 'uz_UZ', 'fifa': 1462.03}, 'Kyrgyzstan': {'locale': 'uz_UZ', 'fifa': 1201.22},
    
}

# --- 2. LEAGUES CONFIGURATION ---

LEAGUES = {
    "ENG_1": {"name": "Premier League", "country": "England", "tier": 1, "teams": 20, "local_weight": 0.5},
    "ESP_1": {"name": "La Liga", "country": "Spain", "tier": 1, "teams": 20, "local_weight": 0.65},
    "USA_1": {"name": "MLS", "country": "USA", "tier": 2, "teams": 18, "local_weight": 0.55},
    "IND_1": {"name": "Indian Super League", "country": "India", "tier": 3, "teams": 12, "local_weight": 0.85},
}