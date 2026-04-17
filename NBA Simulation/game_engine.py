import random

def simulate_game(team1_name, team2_name, teams):
    t1 = teams[team1_name]
    t2 = teams[team2_name]

    score1 = random.randint(85, 130) + (t1["offense"] - t2["defense"]) // 10
    score2 = random.randint(85, 130) + (t2["offense"] - t1["defense"]) // 10

    return score1, score2

def display_results(team1, team2, score1, score2, best_player):
    print(f"\n--- FINAL SCORE ---")
    print(f"{team1}: {score1}  |  {team2}: {score2}")
    winner = team1 if score1 > score2 else team2
    print(f"Winner: {winner}!")
    print(f"Best Player: {best_player['name']} ({best_player['rating']} rating)")