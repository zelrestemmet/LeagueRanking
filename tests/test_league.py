from re import L
import pytest
from typer.testing import CliRunner

from . import *
from league.league import League

@pytest.fixture
def mock_input_file(tmp_path):
    matches = [
        "Lions 3, Snakes 3",
        "Tarantulas 1, FC Awesome 0",
        "Lions 1, FC Awesome 1",
        "Tarantulas 3, Snakes 1",
        "Lions 4, Grouches 0"
    ] 
    matches_file = tmp_path / "matches-input.txt"
    with open(matches_file, "w") as f:
        f.write("\n".join(matches))
    return matches_file
    
@pytest.fixture
def mock_output_file(tmp_path):
    matches = [
        "1. Tarantulas, 6 pts",
        "2. Lions, 5 pts",
        "3. FC Awesome, 1 pt",
        "3. Snakes, 1 pt",
        "5. Grouches, 0 pts",
    ] 
    matches_file = tmp_path / "matches-output.txt"
    with open(matches_file, "w") as f:
        f.write("\n".join(matches))
    return matches_file

def test_add(mock_input_file, mock_output_file):       
    l = League() # INIT LEAGUE CLASS
    l.loadFile(mock_input_file) # LOAD INPUT FILE
    l.sort_scoreboard() # Sorted the score board
    scoreboard = l.get_scoreboard() # Get Scoreboard String

    # Get OUTPUT SAMPLE
    output = None
    with open(mock_output_file, 'r+') as f:
        output = "".join(f.readlines())
        f.close()
   
    # DO COMPARE
    assert scoreboard == output