import random
import csv
from faker import Faker
import teams # Importing the teams module to access locales

if __name__ == "__main__":
    full_db = []
    print("Generating localized football universe...")

    for l_id, conf in teams.LEAGUES.items():
        print(f"-> {conf['name']} ({conf['country']})")
        team_names = teams.generate_league_team_names(conf['country'], conf['teams'])
        
        for i, t_name in enumerate(team_names):
            # Roughly distribute team strengths
            s_tier = 1 if i < 3 else (3 if i > (conf['teams'] - 5) else 2)
            team_obj = teams.Team(t_name, conf, s_tier)
            full_db.extend([p.to_dict() for p in team_obj.players])

    # Save to CSV using the keys of the first entry as headers
    field_names = list(full_db[0].keys())
    with open("data.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(full_db)

    print(f"\nSuccess! 'data.csv' created with {len(full_db)} players.")