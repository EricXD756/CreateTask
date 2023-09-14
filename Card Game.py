#Card Game
P1hand = ['1','1','2','2','3','3','4','4','5','5','6','6','7','7','8','8','9','9','10','10']
P2hand = ['1','1','2','2','3','3','4','4','5','5','6','6','7','7','8','8','9','9','10','10']

def playCard(hand, player, previous_card):
    turn_over = False
    while turn_over == False:
        card = input(player + ", please choose a card to play (1-10), or 'pass' to pass ")
        if card == "pass":
            return(-1)
        if card in hand:
            if int(card) > previous_card:
                print(player + " played a " + card)
                turn_over = True
                hand.remove(str(card))
                print("Your new hand: ", hand)
                return(int(card))
            else:
                print("Card is not higher than previous of: " , previous_card)
        else:
            print("You do not have any " , card, "s")

def playRound(P1hand, P2hand):
    prev_card = -1
    while len(P1hand) > 0 and len(P2hand) > 0:
        prev_card = playCard(P1hand, "Player 1", prev_card)
        if len(P1hand) == 0:
            print("Player 1 wins!")
            break
        prev_card = playCard(P2hand, "Player 2", prev_card)
        if len(P2hand) == 0:
            print("Player 2 wins!")
            break
playRound(P1hand, P2hand)