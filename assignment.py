import random
import itertools

players = ["Josh Bell", "Vladimir Guerrero Jr.", "Pete Alonso", "Joc Pederson", "Carlos Santana", "Matt Chapman", "Alex Bregman", "Ronald Acuna Jr."]
leagueMembers = ["Paul", "Cliff", "Spitz", "Stache", "Buc", "Cole", "Connor", "Jake", "Mawby", "Brad"]

def get_random_pairs(players):
  # Generate all possible non-repeating pairs
  pairs = list(itertools.combinations(players, 2))
 
  # Randomly shuffle these pairs
  random.shuffle(pairs)
  random.shuffle(leagueMembers)
  return pairs

print(get_random_pairs(players))
