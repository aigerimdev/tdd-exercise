from main import blackjack_score
import pytest

#@pytest.mark.skip(reason="no way of currently testing this")
def test_score_for_pair_of_number_cards():
  # Arrange
  hand = [3, 4]
  # Act
  score = blackjack_score(hand)
  # Assert <-- Write assert statement here
  assert score == 7
  
  
def test_facecards_have_values_calculated_correctly():
  hand = ["King", "Queen"]
  
  score = blackjack_score(hand)
  
  assert score == 20

def test_calculates_aces_as_11_where_it_does_not_go_over_21():
  hand = ["Ace", 5, 4]
  
  score = blackjack_score(hand)
  
  assert score == 20
  
def test_calculates_aces_as_1_where_11_would_bust():
  #arrange
  hand = ["Ace", "King", "Queen", 2]
  #Act
  score = blackjack_score(hand)
  #assert
  assert score == "Bust"
  


# @pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_invalid_cards():
  #arrange
  hand = ["Ace", "Joker", 7]
  #act
  score = blackjack_score(hand)
  #assert
  assert score == "Invalid"

def test_returns_invalid_for_list_length_greater_than_5():
  #arrange
  hand = [2, 3, 4, 5, 6, 7]
  #act
  score = blackjack_score(hand)
  #assert
  assert score == "Invalid"

def test_returns_bust_for_scores_over_21():
  #arrange
  hand = ["King", "Queen", "Jack"]
  #act
  score = blackjack_score(hand)
  #assert
  assert score == "Bust"

def test_returns_12_for_ace_ace_king():
  #arrange
  hand = ["Ace", "Ace", "King"]
  #act
  score = blackjack_score(hand)
  #assert
  assert score == 12

def test_returns_14_for_ace_ace_ace_ace():
  #arrange
  hand = ["Ace", "Ace", "Ace", "Ace"]
  #act
  score = blackjack_score(hand)
  #assert
  assert score == 14