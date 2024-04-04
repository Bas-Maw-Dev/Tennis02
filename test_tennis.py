import pytest
from Player import *

class Game:
  def __init__(self, player_1, player_2):
    self.player_1 = Player(player_1.name)
    self.player_2 = Player(player_2.name)
    
  def check_scores(self):
    if self.player_1.score == 40 and self.player_2.score == 40:
      self.player_1.score = "deuce"
      self.player_2.score = "deuce"

@pytest.fixture
def player_1():
  return Player("Player 1")

@pytest.fixture
def player_2():
  return Player("Player 2")

@pytest.fixture
def game(player_1, player_2):
  return Game(Player(player_1.name), Player(player_2.name))

# Each player can have either of these points in one game 0 15 30 40

def test_player_exists(player_1):
  assert player_1.name == "Player 1"
  
def test_player_score_0(player_1):
  assert player_1.score == 0
  
def test_players_in_a_game(game):
  assert game.player_1.name == "Player 1"
  assert game.player_2.name == "Player 2"
  
def test_both_players_score(game):
  game.player_1.score_point()
  game.player_2.score_point()
  assert game.player_1.score == 15
  assert game.player_2.score == 15
  
def test_players_can_score_30(game):
  game.player_2.score = 15
  game.player_2.score_point()
  assert game.player_2.score == 30
  
def test_players_can_score_40(game):
  game.player_1.score = 30
  game.player_1.score_point()
  assert game.player_1.score == 40
  
# If you have 40 and you win the ball you win the game
def test_player_can_win(game):
  game.player_1.score = 40
  game.player_1.score_point()
  assert game.player_1.score == "Win"
  
# If both have 40 the players are deuce
def test_players_in_deuce(game):
  game.player_1.score = 30
  game.player_2.score = 40
  game.player_1.score_point()
  game.check_scores()
  assert game.player_1.score == "deuce"