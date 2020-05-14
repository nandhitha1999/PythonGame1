# THE ROCK-PAPER-SCISSORS-LIZARD-SPOCK GAME


# The main idea of the program is achieved by equating strings
# "rock", "paper", "scissors", "lizard", "Spock" to integer numbers
# The assigments are as follows:

# 0 - rock
# 1 - spock
# 2 - paper
# 3 - lizard
# 4 - scissors


import random
def convert_number_to_name(number):
   
    if number == 0:
        return "rock"
    elif number == 1:
        return "spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return  "lizard"
    elif number == 4:
        return  "scissors"
    else:
        return "ERROR"

    
def convert_name_to_number(name):
   
    if name == "rock":
        return  0
    elif name == "spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "ERROR"

def rpsls(name): 
    
    player_choice = convert_name_to_number(name)
    computer_choice = random.randrange(0, 5)
    
    

    print ("The player chooses :" , name)
    print ("The computer chooses :",convert_number_to_name(computer_choice))
    
    if (computer_choice + 1) % 5 == player_choice:
        print ("PLAYER WINS THE GAME!")
    elif (computer_choice + 2) % 5 == player_choice:
        print ("PLAYER WINS THE GAME!")
    elif computer_choice == player_choice:
        print ("Player and Computer chose same option!\nGAME TIE!")
    else:
        print ("COMPUTER WINS THE GAME!")

        
print("GAME TIME\n")
print("To start game pick your option \nYour Options: \n>> rock\n>> spock\n>> paper\n>> lizard\n>> scissors\n")
player_game = input("Enter your choice : ")
rpsls(str(player_game))
