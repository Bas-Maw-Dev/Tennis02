class Player:
  scores = [0, 15, 30, 40, "Win"]
  
  def __init__(self, name):
    self.name = name
    self.score = Player.scores[0]
    
  def score_point(self):
    self.score = Player.scores[Player.scores.index(self.score) + 1]
    