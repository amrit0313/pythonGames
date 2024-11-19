import random
logo = """"
==================================================
                   BLACKJACK TABLE
==================================================

            Dealer's Hand:  [♠ ]   [ ? ? ]

            Player's Hand:  [♥ ]   [♦  ]

==================================================

           [y] continue     [n] show   

==================================================

"""

def dealCard():
    """Returns a random card from the deck of cards"""
    card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(card)


def calculateScore(cards):
    if sum(cards) ==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) >21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(userScore, computerScore):
    if userScore == computerScore:
        print('draw')
    elif computerScore == 0:
        print("Lose, opponent got a blackjack")
    elif userScore == 0:
        print("hey, you got a blackjack")
    elif userScore >21:
        print('you lose')
    elif computerScore > 21:
        print('you win')     
    elif userScore> computerScore:
        print('you win') 
    else:
        print('you lose')                  

def playGame():
    playerCard =[]
    dealerCard = []
    isGameOver = False 

    for _ in range(2):
        playerCard.append(dealCard())
        dealerCard.append(dealCard()) 

    while not isGameOver:
        userScore = calculateScore(playerCard)
        dealerScore = calculateScore(dealerCard) 
        print(f"the user cards are {playerCard}")
        print(f'dealer first card is {dealerCard[0]}')

        if userScore ==0 or dealerScore == 0 or userScore >21:
            isGameOver = True
        else:
            userDecision = input("type y to take another card and n to pass ")
            if userDecision == 'y':
                playerCard.append(dealCard())
            else:
                isGameOver = True

        
    while dealerScore != 0 and dealerScore<17:
        dealerCard.append(dealCard())
        dealerScore = calculateScore(dealerCard)

    print(f'your final score {userScore}')
    print(f"dealer final score {dealerScore}")
    compare(userScore, dealerScore)    

while input('Type y to play next game, and n to end it here: ') == 'y':
    print(f'{logo}\n')
    playGame()