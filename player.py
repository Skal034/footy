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
