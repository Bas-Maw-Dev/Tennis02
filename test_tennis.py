import pytest

class Player:
  def __init__(self, name):
    self.name = name
    self.score = 0
    
class Game:
  def __init__(self, player_1, player_2):
    self.player_1 = Player(player_1.name)
    self.player_2 = Player(player_2.name)
      

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
  
def test_players_in_a_game(player_1, player_2):
  game = Game(player_1, player_2)
  assert game.player_1.name == "Player 1"
  assert game.player_2.name == "Player 2"
  
  