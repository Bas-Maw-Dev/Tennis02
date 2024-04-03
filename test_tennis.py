import pytest

class Player:
  def __init__(self, name):
    self.name = name
    self.score = 0

@pytest.fixture
def player_1():
  return Player("Player 1")

@pytest.fixture
def player_2():
  return Player("Player 2")

# Each player can have either of these points in one game 0 15 30 40

def test_player_exists(player_1):
  assert player_1.name == "Player 1"
  
def test_player_score_0(player_1):
  assert player_1.score == 0
  
def test_two_players(player_1, player_2):
  assert player_1.name == "Player 1"
  assert player_2.name == "Player 2"
  