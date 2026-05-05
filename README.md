# Final-Project

# NBA Simulation

A simple Python project to simulate NBA games between the Lakers, Celtics, and Warriors. Users can select home and away teams, and the program determines the winner and the best player from the winning team.

## Features
- Choose from three NBA teams: Lakers, Celtics, Warriors
- Simulate a game between any two teams
- Identify the best player on the winning team

## Requirements
- Python 3.7 or higher

## How to Run
1. Open a terminal in the project directory.
2. Run the main script:
   
   ```sh
   python main.py
   ```
3. Follow the prompts to select the home and away teams.

## Project Structure
- `main.py` — Entry point for running the simulation
- `players.py` — Player data and logic for selecting the best player
- `teams.py` — (If used) Team-related logic
- `game_engine.py` — (If used) Game simulation logic

## Customization
- To add more teams or players, edit the `PLAYERS` dictionary in `players.py`.

## Example Output
```
['Lakers', 'Celtics', 'Warriors']
Pick home team: Lakers
['Lakers', 'Celtics', 'Warriors']
Pick away team: Warriors
Winner: Lakers
Best player: LeBron James
```

---
Feel free to expand the simulation with more features, teams, or advanced game logic!
