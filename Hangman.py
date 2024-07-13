import random, hangmanArt, hangmanWords
import os

def clear():
    # Check if the operating system is Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux and macOS, os.name is 'posix'
    else:
        os.system('clear')

print(hangmanArt.logo)
wordList = hangmanWords.words
index = 0
choosenWord = random.choice(wordList)
print(f"the word to guess is {choosenWord}")

display = []

for letters in choosenWord:
    display += "_"
print(display)
length = len(choosenWord)
lives = 7


endOfGame = False
while not endOfGame:
    guess = input("Guess the word: ").lower()
    clear()
    # for x in choosenWord:
    #     if x == guess:
    #         display[index] = x
    #     index += 1
    # print(display)
    for position in range(0, length):
        letter = choosenWord[position]
        if guess  == letter:
            display[position] = letter
       
    print(display)

    if guess not in choosenWord:
         lives -= 1
         print(hangmanArt.hangman_stages[index])
         print(f"{guess.upper()} isnt there on word, you lost a life buddy")
         index +=1
         if lives == 0:
             print("hey hangman tied up, wanna give a new try")
             endOfGame = True    
if "_" not in display:
        print("Damn!!! you guessed it right")
        endOfGame = True
   