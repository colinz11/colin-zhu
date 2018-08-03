import random
import time


deck = []
inGame = True
game= True
firstCardPlayer = 0
secondCardPlayer = 0
playerBusted = False
bits = 10000
bet = 101
highscore = open("highscore.txt", "a") 


def fillDeck():
	for x in range(4):
		for x in range(2, 10):
			deck.append(x)
		for x in range(4):
			deck.append(10)
		deck.append(11)

def shuffle(cards):
    write_index = 0 # to write,
    while write_index < len(cards):
        read_index = random.randint(write_index, len(cards)-1)
        cards[read_index], cards[write_index] = cards[write_index], cards[read_index]
        write_index += 1


def drawCard():
	card = deck[0]
	del deck[0]
	return card


def drawHand(numPlayers):
	for player in range(numPlayers):
		print("Player {0}'s hand:".format(player))
		print(drawCard())
		print(drawCard())

def dealerHand():
	print("Dealer's hand:")
	print(drawCard())

def printHand(hand):
	for card in hand:
		print(card)



def checkScore(hand):
	score = 0
	for card in hand:
		score += card
	if(score > 21):
		return True
	else:
		return False

def displayScore(hand):
	score = 0
	for card in hand:
		score += card
	return score

def printAll(playerHand, dealerHand):
	print("Dealer's hand: ")
	printHand(dealerHand)
	print("Score: " + str(displayScore(dealerHand)))

	print("\n")

	print("Your hand: ")	
	printHand(playerHand)
	print("Score: " + str(displayScore(playerHand)))

def printHidden(dealerCard1, playerHand):
	print("Dealer's hand: ")
	print(dealerCard1)
	print("[ ]")
	
	print("\n")

	print("Your hand: ")	
	printHand(playerHand)
	print("Score: " + str(displayScore(playerHand)))

while bits > 0:
	bet = 1000000000000
	fillDeck()
	shuffle(deck)
	inGame = True
	playerBusted = False

	print("\n")
	print("Do you want to save your score (y/n) Score: " + str(bits))

	quit = input()
	if (quit == "y"):
		print("")
		print("What is your name?")
		name = input()
		highscore.write("\n {0}, score: {1} \n".format(name, bits))
		highscore.write("\n")
		highscore.close()
		read = open("highscore.txt", "r")
		print("\n")
		print("Highscore:")
		print(read.read())		
		read.close()
		break

	print("\n")
	while bet > bits:
		print("Bits: " + str(bits))
		print("How many bits do you want to bet?" )
		try:
			bet = int(input())
		except ValueError:
			print("Invalid Input")

		print("\n")

		if(bet > bits ):
			print("Invalid bet")

	bits -= bet
	print("\n")

	playerCard1 = drawCard()
	dealerCard1 = drawCard()
	playerCard2 = drawCard()
	dealerCard2 = drawCard()
	playerHand = [playerCard1, playerCard2]
	dealerHand = [dealerCard1, dealerCard2]

	printHidden(dealerCard1, playerHand)

	if displayScore(playerHand) == 21:
		inGame = False
		print("")
		print("You got blackjack")
		print("")
		bet = bet * 1.5

	while inGame:
		print("\n")
		print("1. Hit")
		print("2. Stand")
		print("3. Double down")
	
		try:
			choice = int(input())
		except ValueError:
			print("Invalid Input. You lose as punishment")
		print("\n")
	
		if choice == 1:
			playerCardHit = drawCard()
			playerHand.append(playerCardHit)
			printHidden(dealerCard1, playerHand)

			if checkScore(playerHand):
				inGame = False
				playerBusted = True

		elif choice == 2:
			inGame = False
		elif choice == 3:
			if bet <= bits and len(playerHand) == 2:
				playerCardHit = drawCard()
				playerHand.append(playerCardHit)
				printHidden(dealerCard1, playerHand)

				if checkScore(playerHand):
					inGame = False
					playerBusted = True
					bits -= bet
					bet = bet * 2
				else:
					inGame = False
					bits -= bet
					bet = bet * 2
			else:
				print("You don't have enough bits or you already hit")
		else:
			inGame = False
	


	print("\n")
	
	if displayScore(dealerHand) >= 16:
		time.sleep(1)
		printAll(playerHand, dealerHand)


	if playerBusted != True:
		while displayScore(dealerHand) < 16:
			print("")
			time.sleep(1)
			print("The dealer hit")
			print("")
			dealerCardHit = drawCard()
			dealerHand.append(dealerCardHit)
				
			printAll(playerHand, dealerHand)
	
	print("\n")
	

	print("\n")

	if(displayScore(dealerHand) > 21):
		print("The dealer busts. You win")
		won = bet * 2
		print("You won {0} bits".format(won))
		bits += won

	elif(playerBusted):
		print("You busted")
		print("You lost {0} bits".format(bet))
	else:
		if(displayScore(dealerHand) < displayScore(playerHand)):
			print("You win")
			won = bet * 2
			print("You won {0} bits".format(won))
			bits += won
		elif(displayScore(dealerHand) > displayScore(playerHand)):
			print("You lose")
			print("You lost {0} bits".format(bet))
		else:
			print("It's a draw")
			bits += bet

