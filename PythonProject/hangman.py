# DAY 7 HANGMAN
import random
import hangman_words
print(r"""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/       

""")
# create a list of words and define variables


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
     |      /|\
     |       
     |      
     |
 ____|___
"""

hangman3 = r"""
 _______________
     |/      |
     |      (_)
     |      /|\
     |       |
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
     |      / 
     |
 ____|___
"""
hangman5 = r"""
 _______________
     |/      |
     |      (u)
     |      /|\
     |       |
     |      / |
     |
 ____|___
"""
life = 5
wordPlayer=""

#Chose a random country(from module hangman_words) of the list
country = random.choice(hangman_words.listWords).upper()
# print(country)

#Create the empty spaces for the player
wordSelected = list(country)
wordEmpty = []
# print(wordSelected)

for emptySpace in range(len(wordSelected)):
    wordEmpty.append("_")
wordToGuess = " ".join(wordEmpty)
# print(wordEmpty)

# Ask player to select a letter
# wordPlayerList = []
while life > 0:
      if life == 5:
          print(hangman0)
      elif life == 4:
          print(hangman1)
      elif life == 3:
          print(hangman2)
      elif life == 2:
          print(hangman3)
      elif life == 1:
          print(hangman4)
      elif life == 0:
          print(hangman5)

      print("".join(wordEmpty))

      #Check if the player has won
      if "_" not in wordEmpty:
          print("CONGRATULATION YOU WIN!!")
          break

      wordPlayer = input("Guess a letter: ").upper()
      # logic to compare wordPlayerList to wordSelected
      if wordPlayer in wordSelected:
        print(f"attempts left: {life}")
        for index in range(len(wordSelected)):
            if wordSelected[index] == wordPlayer:
                wordEmpty[index] = wordPlayer
      else:
        life -= 1
        print(f"attempts left {life}")

if life == 0:
    print(hangman5)
    print("******GAME OVER YOU LOSE*****")
    print("".join(wordEmpty))
    print(f"The word was {country} ")




















