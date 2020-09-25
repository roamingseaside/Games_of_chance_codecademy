#!/usr/bin/env python
# coding: utf-8
import random
money = 100

#OUTLINES EACH GAME.
print('There are four games available:')
print()
print('   Flip a coin')
print('   Cho han')
print('   Pick a card')
print('   Roulette')
print()
print('If you want to know the rules of the game,')
print('just type rules("<Enter game name here>")')

#OUTLINES THE RULES FOR EACH GAME.
def rules(type):
    if type == 'Flip a coin':
        print('Game: Flip a coin')
        print('Type a guess of "heads" or "tails" and make a bet > 0 and less than what you currently have in your account.')
        print()
        print('Type: coin_flip("guess", bet amount <just use a number>)')
        print('Example: coin_flip("heads", 5)')
    elif type == 'Cho han':
        print('Game: Cho Han:')
        print('The game involves a pair of dice.  Your goal is to guess if the sum equals "even" or "odd."')
        print('Type a guess in the box and make a bet > 0 and less than what you currently have in your account.')
        print()
        print('Type: cho_han("guess", bet amount <just use a number>)')
        print('Example: cho_han("even", 5)')
    elif type == 'Pick a card':
        print('Game:  Pick a card')
        print('You will pick a random card.  Your opponent will pick one as well.   The higher card wins.')
        print('Picking the same value card results in a tie.  You neither win nor lose.')
        print('Make a bet > 0 and less than what you currently have in your account')
        print()
        print('Type: pick_a_card(bet amount <just use a number>)')
        print('Example: pick_a_card(5)')
    elif type == 'Roulette':
        print('Game: Roulette')
        print(' game rules to be written')
        print()
        print('Type: roulette("guess", bet amount <just use a number>)')
    else:
        print('Are you sure you typed the name in correctly?')
        print('Capitalization and spacing matter!!')

###----------------------------------------------------------------------------------------------------------
###Coin flip function
def coin_flip(guess, bet):
    global money 
    num = random.randint(1,2)
    if guess != 'heads' and guess != 'tails':
        print('Did you enter the guess correctly? Only "heads" or "tails" is accepted.')
        print('NOTE: guess is case sensitive')
    elif bet < 1:
        print('Shame on you...you can not play if you do not bet correctly.')
    elif money - bet < 0:
        print('Sorry...you are too poor to make that bet.  Your current balance is $'+str(money))
    else:
        if num == 1:
            outcome = 'heads'
        else:
            outcome = 'tails'
        if outcome == guess:
            money += bet
            print('You guessed right.  You win $'+str(bet)+' and you now have $'+str(money))
        else:
            money -= bet
            print('You guessed wrong.  You lose $'+str(bet)+' and you now have $'+str(money))
###----------------------------------------------------------------------------------------------------------
###Cho han function
def cho_han(guess, bet):
    global money
    answer = 0
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    if guess != 'even' and guess != 'odd':
        print('Did you enter the guess correctly? Only "even" or "tails" is accepted.')
        print('NOTE: guess is case sensitive')
    elif bet < 1:
        print('Shame on you...you can not play if you do not bet correctly.')
    elif money - bet < 0:
        print('Sorry...you are too poor to make that bet.  Your current balance is $'+str(money))
    else:
        if total%2 == 0:
            answer = 'even'
        else:
            answer = 'odd'
        if guess == answer:
            money += bet
            print('You guessed right.  You win $'+str(bet)+' and you now have $'+str(money))
        else:
            money -= bet
            print('You guessed wrong.  You lose $'+str(bet)+' and you now have $'+str(money))
###----------------------------------------------------------------------------------------------------------
##pick a card fuction
##ties currently reset the deck.  Next iteration show have the ability to pull from a deck using a list and reduct the probability.
def pick_a_card(bet):
    global money
    player = random.randint(2,14)
    opponent = random.randint(2,14)
    if bet < 1:
        print('Shame on you...you can not play if you do not bet correctly.')
    elif money - bet < 0:
        print('Sorry...you are too poor to make that bet.  Your current balance is $'+str(money))
    else:
        if player > opponent:
            money += bet
            print('Your card was HIGHER.  You win $'+str(bet)+' and you now have $'+str(money))
        elif player < opponent:
            money -= bet
            print('You lost.  You lose $'+str(bet)+' and you now have $'+str(money))
        else:
            print('It was a tie.  Nothing happens')



rules('Cho han')
print()
coin_flip('tails', 25)  
print()
cho_han('odd',35)

pick_a_card(160)



pick_a_card(155)





