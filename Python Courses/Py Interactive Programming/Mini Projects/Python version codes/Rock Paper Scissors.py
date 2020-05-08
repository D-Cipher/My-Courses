# Rock-paper-scissors-lizard-Spock
#Enjoy the game :)
#Yours, D'Cypher

#sissors > paper
#Paper > rock
#Rock > lizard
#Lizard > Spock
#Spock > Sissors
#Sissors > lizard
#Lizard > paper
#Paper > Spock
#Spock > rock
#rock > sissors

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print("Error")


def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print("Error")

import random
def rpsls(player_choice):
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)

    print(" ")
    print("Player Chooses:", player_choice)
    print("Computer Chooses:", comp_choice)

    winner = (player_number - comp_number)%5

    if winner == 0:
        print("----Result: Tie Game.")
    if winner == 1:
        print("----Result: You Win.")
    if winner == 2:
        print("----Result: You Win.")
    if winner == 3:
        print("----Result: Computer Wins.")
    if winner == 4:
        print("----Result: Computer Wins.")

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

#print "secret number is" , cpu_number
