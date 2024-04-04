class Player:
  scores = [0, 15, 30, 40, "Win"]
  deuce_scores = ["deuce", "advantage", "Win"]
  
  def __init__(self, name):
    self.name = name
    self.score = Player.scores[0]
    
  def score_point(self):
    if self.score in Player.scores:
      self.score = Player.scores[Player.scores.index(self.score) + 1]
    else:
      self.score = Player.deuce_scores[Player.deuce_scores.index(self.score) + 1]