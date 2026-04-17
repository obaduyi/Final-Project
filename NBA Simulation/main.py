from teams import TEAMS, choose_team
from players import get_best_player
from game_engine import simulate_game, display_results

def main():
    while True:
        print("\n=== NBA GAME SIMULATOR ===")
        team1 = choose_team("Pick home team: ")
        team2 = choose_team("Pick away team: ")

        score1, score2 = simulate_game(team1, team2, TEAMS)
        winner = team1 if score1 > score2 else team2
        best = get_best_player(winner)

        display_results(team1, team2, score1, score2, best)

        again = input("\nPlay again? (y/n): ")
        if again.lower() != "y":
            break

if __name__ == "__main__":
    main()