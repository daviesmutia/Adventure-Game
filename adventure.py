import time
import random

creature = ["Raccoon", "Donkey", "Troll", "Panda", "Bear"]
weapon = []


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    global enemy
    enemy = random.choice(creature)
    print_pause("You find yourself in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere "
                "around here, and has been terrifying "
                "the nearby village.")
    print_pause("In front of you is house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not effective) dagger.")


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause("Enter a valid input.\n")


def house():
    print_pause("\nYou approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                f"and out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")
    print_pause("You feel a bit under-prepared for this, "
                "with only having a tiny dagger.")


def cave(weapon):
    print_pause("You peer cautiosly into the cave.")
    if "sword" not in weapon:
        print_pause("It turns out to be only a very small cave.")
        print_pause("You eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical sword of Ogoroth!")
        print_pause("you discard your silly old dagger "
                    "and take the sword with you.")
        weapon.append("sword")
        field()
    else:
        print_pause("You've been here and gotten all the good stuff "
                    "It's just an empty cave now.")
        field()


def fight():
    fight_choice = valid_input("Would you like to "
                               "(1) fight or (2) run away?", ['1', '2'])
    if fight_choice == '1':
        if "sword" in weapon:
            print_pause(f"\nAs the {enemy} moves to attack, "
                        "you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your hand "
                        "as you brace yourself for the attack.")
            print_pause(f"But the {enemy} takes one look at your "
                        "new shiny toy and runs away!")
            print_pause(f"You have rid the town of the {enemy}."
                        "You are victorious!\n")
            play_game_again()
        else:
            print_pause("You do your best...")
            print_pause(f"but your dagger is no match for the {enemy}.")
            print_pause("You have been defeated!")
            play_game_again()
    else:
        print_pause("You run back to the field. "
                    "Luckily, you don't seem "
                    "to have been followed.\n")
        game(weapon)


def field():
    print_pause("You walk back out to the field.")
    game(weapon)


def play_game_again():
    play_again = valid_input("Would you like to play again? (y/n)", ['y', 'n'])
    if play_again == 'y':
        global enemy
        enemy = random.choice(creature)
        print_pause("\nExcellent!! Restarting the game ...")
        intro()
        game(weapon)
    else:
        print_pause("Thank you for playing. See you next time. Adios!!")


def game(weapon):
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    game_choice = valid_input("(Please enter 1 or 2)", ['1', '2'])
    if game_choice == '1':
        house()
        fight()
    else:
        cave(weapon)
        game(weapon)


def main(weapon):
    intro()
    game(weapon)
    play_game_again()


main(weapon)
