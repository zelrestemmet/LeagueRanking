from pathlib import Path
from typing import Any, Dict, List, NamedTuple
import more_itertools


class League:
    def __init__(self) -> None:
        self.scoreboard = dict()
        
    def setLeague(self, lines: list[str]) -> None:
        # loop through board and dertermin win, lose or tie (draw) and append to team list
        for line in lines:
            # split teams and scores for each line
            subs = line.split(',') # Split Into Teams 1 and 2

            # Team 1 Data
            team1info = subs[0]
            team1infoSplit = team1info.rsplit(" ", 1)
            team1 = team1infoSplit[0]
            score1 = int(team1infoSplit[1])

            # Team 2 Data
            team2info = subs[1]
            team2infoSplit = team2info.rsplit(" ", 1)
            team2 = team2infoSplit[0]
            score2 = int(team2infoSplit[1])

            # Check State (calculate win, lose, and tie)
            tie = score1 == score2
            team1Win = score1 >= score2
            team2Win = score1 < score2

            # Init Teams                        
            if team1 not in self.scoreboard:
                self.scoreboard[team1] = 0                
            if team2 not in self.scoreboard:
                self.scoreboard[team2] = 0
            
            # Update State
            if tie:
                self.scoreboard[team1] = self.scoreboard[team1] + 1
                self.scoreboard[team2] = self.scoreboard[team2] + 1
            elif team1Win:
                self.scoreboard[team1] = self.scoreboard[team1] + 3
            elif team2Win:
                self.scoreboard[team2] = self.scoreboard[team2] + 3

    def loadFile(self, path) -> None:
        lines = []
        with open(path, "r+") as f:
            lines = f.readlines()
        self.setLeague(lines)

    def sort_scoreboard(self) -> None:
        """Sort the league score list."""
        scoreboard = {}
        inner_sorted = sorted(self.scoreboard.items(), key=lambda team: (-team[1], team[0]))
        for x in inner_sorted:
            scoreboard[x[0]] = x[1]
        self.scoreboard = scoreboard

    def get_scoreboard(self) -> str:
        """Return the league score list."""
        # create a new dict with ranks
        scoreboard_sorted = sorted(((v, k) for k, v in self.scoreboard.items()), reverse=True)
        ranks = {scoreboard_sorted[0][1]: 1}
        rank = 1      # current rank
        streak = 0    # keep track of how many in a row are the same rank
        for (score1, team1), (score2, team2) in more_itertools.pairwise(scoreboard_sorted):
            if score2 < score1:
                rank += 1
                ranks[team2] = rank + streak
                streak = 0
            else:
                streak += 1
                ranks[team2] = rank
        scoreboard_array = []   
        for key, value in self.scoreboard.items():
            scoreboard_array.append("{counter}. {team}, {points} {pointsstring}".format(counter=ranks[key], team=key.lstrip(), points=value, pointsstring= "pt" if value is 1 else "pts").lstrip())
        return "\n".join(scoreboard_array)
