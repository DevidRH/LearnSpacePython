#ANCHOR - Coin Toss Randomisation
import random

random_coint = random.randint(0,1)      #NOTE - random integer 0 sampai 1

if random_coint == 0:
  print("Heads")
else:
  print("Tails")