import time
import random

random_weapons = ["sword", "axe", "spoon", "bow"]
monsters = ["dragon", "troll", "pirate", "elf"]
monster = ""


def print_pause(message):
    print(message)
    time.sleep(1.1)


def choose_between_two_options(option1, option2):
    choice = ""
    while choice != option1 and choice != option2:
        choice = str(input("(Please enter " + str(option1) +
                           " or " + str(option2) + ").\n")).lower()
    return choice


def play_again():
    print_pause("Would you like to play again? (y/n)")
    option = choose_between_two_options("y", "n")
    if option == "y":
        print_pause("Excellent! Restarting the game ...")
        intro()
    else:
        print_pause("Thanks for playing! See you next time.")


def intro():
    global monster
    monster = random.choice(monsters)
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + monster + " is somewhere around here,"
                " and has been terrifying the nearby village.")
    house("dagger")


def fight(weapon):
    if weapon == "dagger":
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the dragon.")
        print_pause("You have been defeated!")
    else:
        print_pause("As the dragon moves to attack, you unsheath your new " +
                    weapon + ".")
        print_pause("The " + weapon[:1].upper() + weapon[1:] + " of Ogoroth "
                    "shines brightly in your hand as you brace yourself"
                    "for the attack.")
        print_pause("But the " + monster +
                    " takes one look at your shiny new toy and runs away!")
        print_pause("You have rid the town of the " + monster +
                    ". You are victorious!")
    play_again()


def cave(weapon):
    if weapon == "dagger":
        weapon = random.choice(random_weapons)
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical " + weapon[:1].upper() +
                    weapon[1:] + " of Ogoroth!")
        print_pause("You discard your silly old dagger and take the " +
                    weapon + " with you.")
    else:
        print_pause("You've been here before, and gotten all the good stuff."
                    " It's just an empty cave now.")
    print_pause("You walk back out to the field.\n")
    house(weapon)


def house(weapon):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do? ")
    option = choose_between_two_options("1", "2")
    if option == "1":
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens "
                    "and out steps a " + monster + ".")
        print_pause("Eep! This is the " + monster + "'s house!")
        print_pause("The " + monster + " attacks you!")
        if weapon == "dagger":
            print_pause("You feel a bit under-prepared for this,"
                        " what with only having a tiny dagger.")
        print_pause("Would you like to (1) fight or (2) run away?")
        option = choose_between_two_options("1", "2")
        if option == "1":
            fight(weapon)
        else:
            print_pause("You run back into the field. Luckily,"
                        " you don't seem to have been followed.\n")
            house(weapon)
    else:
        cave(weapon)


intro()
