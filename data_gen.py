import random
import csv
from faker import Faker
import teams # Importing the teams module to access locales

if __name__ == "__main__":
    full_db = []
    print("Generating football universe...")

    for l_id, conf in teams.LEAGUES.items():
        print(f"-> {conf['name']} ({conf['country']})")
        team_names = teams.generate_league_team_names(conf['country'], conf['teams'])
        
        for i, t_name in enumerate(team_names):
            # Roughly distribute team strengths
            team_tier = round(random.triangular(-2, 2, 0)) # More teams in the middle tiers
            print(f"   - Team: {t_name} (Tier: {team_tier:.2f})")
            team_obj = teams.Team(t_name, conf, team_tier)
            full_db.extend([p.to_dict() for p in team_obj.players])

    # Save to CSV using the keys of the first entry as headers
    field_names = list(full_db[0].keys())
    with open("data.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(full_db)

    print(f"\nSuccess! 'data.csv' created with {len(full_db)} players.")