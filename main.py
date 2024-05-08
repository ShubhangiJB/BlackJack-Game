from replit import clear 
from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

play_more = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

while play_more == "y":
  clear()
  
  print(logo)
  
  player_cards = []
  
  player_cards.append(deal_card())
  player_cards.append(deal_card())
  player_score = 0
  
  for score in player_cards:
    player_score += score
  
  print(f"Your cards: {player_cards}, current score: {player_score}")
  
  dealer_score = 0
  dealer_cards = []
  dealer_card = deal_card()
  dealer_cards.append(dealer_card)
  dealer_score += dealer_card
  
  print(f"Computer's first card: {dealer_cards}")
  want_card = input("Type 'y' to get another card, type 'n' to pass: ")
  
  while want_card == "y" and player_score<21:
    player_cards.append(random.choice(cards))
    player_score = 0
    for score in player_cards:
      player_score += score
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {dealer_cards}")
    want_card = input("Type 'y' to get another card, type 'n' to pass: ")
  
  print(f"Your final hand: {player_cards}, final score: {player_score}")
  
  while dealer_score<21:
    dealer_card = random.choice(cards)
    dealer_cards.append(dealer_card)
    dealer_score += dealer_card
  
  print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
  
  if player_score>21:
    print("You went over. You lose.")
  elif dealer_score>21:
    print("Opponent went over. You win.")
  elif player_score==dealer_score:
    print("It's a draw.")
  elif player_score>dealer_score:
    print("You win.")
  else:
    print("You lose.")
  
  play_more = input("Type 'y' if you want to play again, else type 'n': ")
