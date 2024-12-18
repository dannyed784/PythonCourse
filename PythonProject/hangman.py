# DAY 7 HANGMAN
import random

# create a list of words and define variables
listWords = ["Canada","Sweden","USA","Cuba","Colombia","France","Maroc",
             "Spain","Japan","China","Russia","Philippines","Australia","England",
             "Chile","Mexico","Poland","Germany","Italy","Mali","Egypt",
             "Greece","Thailand","Costa Rica","South Korea","New Zeeland","Iceland"]

hangman0 = r"""
 _______________
     |/      |
     |      
     |      
     |       
     |      
     |
 ____|___
"""
hangman1 = r"""
 _______________
     |/      |
     |      (_)
     |      
     |      
     |      
     |
 ____|___
"""
hangman2 = r"""
 _______________
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
 ____|___
"""

hangman3 = r"""
 _______________
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
 ___|___
"""
hangman4 = r"""
 _______________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
 ____|___
"""
hangman5 = r"""
 _______________
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / |
     |
 ____|___
"""

#Create a variable call life
life = 5
#Chose a random country of the list
country = random.choice(listWords)
print(country)

#Create the empty spaces for the player
wordSelected = list(country)
wordEmpty = []
print(wordSelected)

for emptySpace in range(len(wordSelected)):
    wordEmpty.append("_")
wordToGuess = " ".join(wordEmpty)
print(wordEmpty)


# Ask the player to select a letter
wordPlayerList = []
while life >= 0:
      if life == 5:
          print(hangman0)
          print("".join(wordEmpty))
      elif life == 4:
          print(hangman1)
          print("".join(wordEmpty))
      elif life == 3:
          print(hangman2)
          print("".join(wordEmpty))
      elif life == 2:
          print(hangman3)
          print("".join(wordEmpty))
      elif life == 1:
          print(hangman4)
          print("".join(wordEmpty))
      elif life == 0:
          print(hangman5)
          print("".join(wordEmpty))

      wordPlayer = input("Guess a letter: ")
      # logic to compare wordPlayerList to wordSelected
      if wordPlayer in wordSelected:
        print("Yes")
        for index in range(len(wordSelected)):
            if wordSelected[index] == wordPlayer:
                wordEmpty[index] = wordPlayer
      else:
        print("No")
        life -= 1

print("GAME OVER YOU LOSE")
# print(wordEmpty)
# print("".join(wordEmpty))



















