"""
Χρησιμοποιείστε τον κώδικα που έχουμε φτιάξει για “21” (card game) και υπολογίστε σε πόσα από τα 100 παιχνίδια κερδίζει ο πρώτος παίκτης,
σε πόσα ο δεύτερος, και σε πόσα έχουμε ισοπαλία.
Στη συνέχεια, πειράξτε το μοίρασμα ώστε ο πρώτος παίκτης να ξεκινάει με 10 ή φιγούρα (J,Q, K) και ο δεύτερος ποτέ με 10 ή φιγούρα.
Υπολογίστε τα νέα στατιστικά για 100 τυχαία παιχνίδια, δηλαδή πόσα κερδίζει ο πρώτος παίκτης, πόσα ο δεύτερος, και σε πόσα έχουμε ισοπαλία.
Κάθε φορά το μοίρασμα των χαρτιών γίνεται από την αρχή και ανακατεύεται η τράπουλα.
"""


import random

cards = []
cardsP1 = []
cardsP2 = []
figures = ["J", "Q", "K"]
card = [i for i in range(1, 11)] + figures
cardP1 = [i for i in range(11, 11)] + figures
cardP2 = [i for i in range(1, 10)]
color = ["H", "S", "C", "D"]

# both players start randomly
sumWin1 = 0
sumWin2 = 0
sumDraw = 0
repeat = 0
while repeat < 100:
    repeat += 1
    # print(rp)
    for i in card:
        for j in color:
            cards.append([i, j])
    random.shuffle(cards)
    # print("P1 joins the game")
    player1 = []
    sum1 = 0
    while sum1 < 16:
        sum1 = 0
        player1.append(cards.pop())
        # print (player1)
        for card in player1:
            if card[0] in figures:
                sum1 = sum1+10
            else:
                sum1 = sum1+card[0]
        # print(sum1)
    # if sum1>21:
        # print("P2 wins!")
    # else:
    if sum1 <= 21:
        # print("P2 joins the game") #let me add one more player
        player2 = []
        sum2 = 0
        while sum2 < 16:
            sum2 = 0
            player2.append(cards.pop())
            # print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2 = sum2+10
                else:
                    sum2 = sum2+card[0]
            # print(sum2)
        if sum2 > 21:
            sum2 = 0
        if sum1 > sum2:
            # print("P1 wins!")
            sumWin1 += 1
        # elif sum2>sum1:
            # print("P2 wins!")
        else:
            sumDraw += 1
            # print("draw!")
print("Results after 100 rounds:")
sumW2 = 100-sumWin1-sumDraw
print("Draws:")
print(sumDraw)
print("Total wins P1:")
print(sumWin1)
print("Total wins P2:")
print(sumW2)

print("NEW GAME")

# Player 1 always starts with 10 Player 2 never 10
sumWin1 = 0
sumWin2 = 0
sumDraw = 0
repeat = 0
while repeat < 100:
    repeat += 1
    for i in card:
        for j in color:
            cards.append([i, j])
    random.shuffle(cards)
    for i in cardP1:
        for j in color:
            cardsP1.append([i, j])
    random.shuffle(cardP1)
    for i in cardsP2:
        for j in color:
            cardsP2.append([i, j])
    random.shuffle(cardsP2)
    # print("P1 joins the game")
    player1 = []
    sum1 = 0
    firstCardP1 = 0
    while sum1 < 16:
        sum1 = 0
        if firstCardP1 == 0:
            player1.append(cardP1.pop())
            firstCardP1 = 1
        else:
            player1.append(cards.pop())
        # print (player1)
        for card in player1:
            if card[0] in figures:
                sum1 = sum1+10
            else:
                sum1 = sum1+card[0]
        # print(sum1)
    # if sum1>21:
        # print("P2 wins!")
    # else:
    if sum1 <= 21:
        # print("P2 joins the game") #let me add one more player
        player2 = []
        sum2 = 0
        firstCardP2 = 0
        while sum2 < 16:
            sum2 = 0
            if firstCardP2 == 0:
                player2.append(cardsP2.pop())
                firstCardP2 = 1
            else:
                player2.append(cards.pop())
            # print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2 = sum2+10
                else:
                    sum2 = sum2+card[0]
            # print(sum2)
        if sum2 > 21:
            sum2 = 0
        if sum1 > sum2:
            # print("P1 wins!")
            sumWin1 += 1
        # elif sum2>sum1:
            # print("P2 wins!")
        else:
            sumDraw += 1
            # print("draw!")
print("New results after 100 rounds: ")
sumW2 = 100-sumWin1-sumDraw
print("Draws:")
print(sumDraw)
print("P1 Wins:")
print(sumWin1)
print("P2 wins:")
print(sumWin2)
