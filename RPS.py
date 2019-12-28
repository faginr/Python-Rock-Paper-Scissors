import random
import time

def compData():
    global compInput
    # start game
    print("Starting Rock-Paper-Scissors Game...")
    # generate computer input
    compInput = random.randint(1,3)
def setup():
    global userInput
    # gather user input
    print ("Please Select:\n 1)Rock \n 2)Paper \n 3)Scissors")
    # validate input
    inputflag = True
    while inputflag:
        userInput = input(">")
        if userInput.isdigit():
            userInput = int(userInput)
            if userInput > 0 and userInput < 4:
                print("Ready?")
                time.sleep(.5)
                print (".")
                time.sleep(.5)
                print (".")
                time.sleep(.5)
                print (".")
                print("Go!")
                inputflag = False
            else:
                print("Invalid Selection, Please select again.")
        else:
                print("Invalid Selection, Please select again.")


def game():
    # compare values and print results
    if compInput == 1:
        # comp rock
        if userInput == 1:
            print ("Player: Rock")
            time.sleep(.8)
            print ("Computer: Rock")
            time.sleep(.8)
            print ("tie, go again.")
            div()
        elif userInput == 2:
            print ("Player: Paper")
            time.sleep(.8)
            print ("Computer: Rock")
            time.sleep(.8)
            print ("Paper beats Rock, Player wins!")
        else:
            print ("Player: Scissors")
            time.sleep(.8)
            print ("Computer: Rock")
            time.sleep(.8)
            print ("Rock beats Paper, Computer wins!")
    elif compInput == 2:
        # comp paper
        if userInput == 1:
            print ("Player: Rock")
            time.sleep(.8)
            print ("Computer: Paper")
            time.sleep(.8)
            print ("Paper beats Rock, Computer wins!")
        elif userInput == 2:
            print ("Player: Paper")
            time.sleep(.8)
            print ("Computer: Paper")
            time.sleep(.8)
            print ("tie, go again.")
            div()
        else:
            print ("Player: Scissors")
            time.sleep(.8)
            print ("Computer: Paper")
            time.sleep(.8)
            print ("Scissors beats Paper, Player wins!")
    else:
        # comp scissors
        if userInput == 1:
            print ("Player: Rock")
            time.sleep(.8)
            print ("Computer: Scissors")
            time.sleep(.8)
            print ("Rock beats Scissors, Player wins!")
        elif userInput == 2:
            print ("Player: Paper")
            time.sleep(.8)
            print ("Computer: Scissors")
            time.sleep(.8)
            print ("Scissors beats Paper, Computer wins!")
        else:
            print ("Player: Scissors")
            time.sleep(.8)
            print ("Computer: Scissors")
            time.sleep(.8)
            print ("tie, go again.")
            div()
    # restart or quit

def div():
    compData()
    setup()
    game()
div()
