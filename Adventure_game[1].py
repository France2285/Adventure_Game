import time
import sys
import random


list_noun = (["Wizard", "Zwerg", "Mitt crunch",
              "Minotor", "Cyclope", "Dragon", "Gargoyle"])


def random_noun():
    n = random.randint(0, 6)
    return list_noun[n]


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("Welcome in the Castle of the 3 Dragons")
    print_pause("Your quest is to save the Fairy locked "
                "in the tower of the castle ")
    print_pause("Your enter in the Castle and in front of you "
                "there is 3 doors.")


def door_number1(items):
    if "potion" in items:
        print_pause("Sorry, there is nothing here! "
                    "go back to the doors!")
    else:
        potion = ""
        while potion != "green" and potion != "red":
            print_pause("The "+random_noun()+" of all time stands before "
                        "you with two magic potions. "
                        "Could you please choose one?")
            potion = input("The green one \n"
                           "or the red one? ")
        if potion == "green":
            print_pause("Oh! no! You chose the wrong one!")
            print_pause("You just explosed, you are dead!")
            lose_game()
        elif potion == "red":
            print_pause("Wahou! You become super strong with this potion.")
            print_pause("you can go back to the doors!")
            items.append("potion")
        else:
            print_pause("Oups, I do not understand what do you mean!")
    door_castle(items)


def door_number2(items):
    if "small book" in items:
        print_pause("Sorry, but there is nothing here!")
    else:
        response = ""
        while response != "run" and response != "fight":
            print_pause("You just enter in the room of a "+random_noun())
            print_pause("You have the choice to fight or to run! "
                        " What do you choose?")
            response = input("run or fight?").lower()
        if response == "run":
            print_pause("Too late the Monster is"
                        " away to big for you. You are dead!")
            lose_game()
        elif response == "fight":
            if "potion" in items:
                print_pause("Yeah, you are so fast and"
                            " so strong with this potion.")
                print_pause("The Monster is completly done."
                            " You won a small book")
                items.append("small book")
            else:
                print_pause("The big Monster is too strong,"
                            " he eats you. You are dead!!")
                lose_game()
    door_castle(items)


def door_number3(items):
    response1 = ""
    print_pause("Wahou you reach the Tower with the Fairy."
                " But There is a big "+random_noun())
    print_pause("You have the choice to fight or to speak! "
                " What do you choose?")
    while response1 != "fight" and response1 != "speak":
        response1 = input("fight or speak?").lower()
    if response1 == "fight":
        print_pause("NO!!! He doesn't like to fight!"
                    "He push you and you fall from the tower!")
        lose_game()
    else:
        if "small book" in items:
            print_pause("Because of the small book,"
                        " you understand everything, and starting"
                        " to be his best friend")
            print_pause("Congratulation, you convinced "
                        "him to release the Fairy.")
            print_pause("You won the game!")
            play_again()
        else:
            print_pause("The dragon doesn't understand you, and kill you.")
            lose_game()
    door_castle(items)


def lose_game():
    print_pause("!!!! GAME OVER !!!!")
    play_again()


def play_again():
    answer = ""
    print_pause("Do you want to play again?")
    while answer != "yes" and answer != "no":
        answer = input("Answer Yes or No ").lower()
    if answer == "yes":
        play_game()
    else:
        print("OK. Have a nice day!")
        sys.exit()


def door_castle(items):
    door = ""
    while door not in ["1", "2", "3"]:
        print_pause("Please choose the number of the door?")
        door = input("Door number 1?\n"
                     "Door number 2?\n"
                     "Door number 3?")
    if door == "1":
        print_pause("You choose the door number ONE")
        door_number1(items)
    elif door == "2":
        print_pause("You choose the door number TWO")
        door_number2(items)
    elif door == "3":
        print_pause("You choose the door number THREE")
        door_number3(items)


def play_game():
    items = []
    intro()
    door_castle(items)


play_game()
