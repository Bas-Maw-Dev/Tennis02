class Player:
  def __init__(self, name):
    self.name = name

# Each player can have either of these points in one game 0 15 30 40

def test_player_exists():
  player_1 = Player("Player 1")
  assert player_1.name == "Player 1"