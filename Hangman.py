import random

wordList = ['try', 'unknown', 'shahrukh', 'brain', 'she', 'engineer']

choosenWord = random.choice(wordList)

guess = input("Guess the word").lower()

for letter in choosenWord:
    if letter == guess:
        print("Right")
    else:
        print("wrong")




