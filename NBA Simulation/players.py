PLAYERS = {
    "Lakers": [
        {"name": "LeBron James", "rating": 95},
        {"name": "Anthony Davis", "rating": 90}
    ],
    "Celtics": [
        {"name": "Jayson Tatum", "rating": 92},
        {"name": "Jaylen Brown", "rating": 88}
    ],
    "Warriors": [
        {"name": "Stephen Curry", "rating": 96},
        {"name": "Klay Thompson", "rating": 87}
    ]
}

def get_best_player(team_name):
    players = PLAYERS[team_name]
    return max(players, key=lambda p: p["rating"])
