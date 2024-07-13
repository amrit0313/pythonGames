import random

wordList = ['try', 'unknown', 'shahrukh', 'brain', 'she', 'engineer']
# index = 0
choosenWord = random.choice(wordList)
print(f"the word to guess is {choosenWord}")
display = []
for letters in choosenWord:
    display += "_"
print(display)
endOfGame = False
while not endOfGame:
    guess = input("Guess the word: ").lower()
    length = len(choosenWord)

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

    if "_" not in display:
        print("Damn!!! you guessed it right")
        endOfGame = True