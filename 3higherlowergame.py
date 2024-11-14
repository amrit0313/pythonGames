import random

celebrties = {
    'shahrukh khan':47.9,
    'sonu nigam':2.8,
    'andre russel':3.8,
    'virat kohli': 271,
    'selena gomez': 400,
    'cristiano ronaldo':600,
    'amrit':700,
    'eva elfie':4.5, 
    'annonymous person': 770,
    }
firstceleb = random.choice(list(celebrties.keys()))
secondceleb= random.choice(list(celebrties.keys()))
if secondceleb == firstceleb:
    secondceleb= random.choice(list(celebrties.keys()))

print("Let's  go to Higher Lower game: ")
gameOver = False
def playGame():
    def compare():
        if celebrties[firstceleb]> celebrties[secondceleb]:
            return firstceleb
        else:
            return secondceleb

    def change(higherOne):
        global firstceleb, secondceleb
        if higherOne ==firstceleb:
            secondceleb = random.choice(list(celebrties.keys()))
            if secondceleb == higherOne:
                secondceleb = random.choice(list(celebrties.keys()))
        else:
            firstceleb = random.choice(list(celebrties.keys()))
            if firstceleb == higherOne:
                firstceleb = random.choice(list(celebrties.keys()))



            
    print(f'{firstceleb} & {secondceleb}')
    choosen = input('Guess who has more followers: ')
    if choosen == compare():
        print('hey! you got it right ')
        change(choosen)
    else:
        print('you lost ')
        global gameOver
        gameOver =True
            


while not gameOver:
    playGame()