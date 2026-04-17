TEAMS = {
    "Lakers": {"offense": 112, "defense": 108},
    "Celtics": {"offense": 118, "defense": 105},
    "Warriors": {"offense": 115, "defense": 110},
    # ... add all 30 teams
}

def choose_team(prompt):
    print(list(TEAMS.keys()))
    choice = input(prompt)
    return choice if choice in TEAMS else None