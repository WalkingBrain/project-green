import engine as game
from time import sleep

def red_text(string):
    return f"\033[31m{string}\033[0m"  # ANSI escape code for red text

def blue_text(string):
    return f"\033[34m{string}\033[0m"  # ANSI escape code for blue text

def green_text(string):
    return f"\033[32m{string}\033[0m"  # ANSI escape code for green text

def yellow_text(string):
    return f"\033[33m{string}\033[0m"  # ANSI escape code for yellow text

def purple_text(string):
    return f"\033[95m{string}\033[0m"  # ANSI escape code for light purple text



def title_screen():
    global player_name
    

skip = (input("Do you want to skip dialogue? For story I recomend to say no. Yes/No: "))

if skip == "No":
    print("Welcome, traveler.\n")
    sleep(2)
    print("You are lost in a dark forest.")
    sleep(4)
    print("Oh, yes, I forgot to introduce myself.")
    sleep(4)
    print(f"I am {purple_text("Aetherion")}, the ruler of this forest.")
    sleep(4)
    print("You might be wondering why you're here.")
    sleep(4)
    print("One shall find the reason for struggle after they have defeated it.")
    sleep(4)
    print("There is a path out, but you can see a shadowy figure ahead.")
    player_name = input("How should I refer to you? ")
    sleep(4)
    print(f"Yet again, welcome, {game.red_text(player_name)}.\n")
    sleep(4)
    print(f"You identify the shadowy figure as a {game.yellow_text('skeleton')}.")
    sleep(4)
    print("You wield an old, rusty sword.")
    sleep(4)
    print("It has definitely seen better days, but using it is your only option.")
    sleep(4)
    print(f"{game.red_text(player_name)}, we shall meet again.")
    sleep(4)
    print("And there, your adventure starts.\n")
    sleep(12)

elif skip == "Yes":
    print("You skippped the dialogue!")
    sleep(4)
    player_name = input("What is your name? ")
    sleep(4)
    print("And there, your adventure starts.\n")
    sleep(12)
    

def initialize_game(player_name):
    global player, skeleton, zombie, rusty_sword, sword

    player = game.Player(player_name, 100, 0, 5, 20, 50, 1, 0, 100)

    skeleton = game.Enemy("Skeleton", 50, 0, 10, 20, 50, 1, 40)
    zombie = game.Enemy("Zombie", 75, 0, 15, 25, 50, 1, 60)

    skeleton.is_alive = False
    zombie.is_alive = False

    rusty_sword = game.Weapon("Rusty Sword", 10, 20, 50, 1, 0, 75)
    sword = game.Weapon("Sword", 15, 30, 60, 1, 0, 80)

    player.obtain_item(rusty_sword)

    print("With that in mind, your first fight shall come along.\n")
    sleep(4)

def first_kill():
    sleep(2)
    print("\nYou killed the skeleton!")
    sleep(6)
    print("Though you are now a murderer, you are on the right path.")
    sleep(2)
    print("I shall reward you for your actions later, but for now, you may continue your journey.\n")
    sleep(12)

def second_kill():
    sleep(2)
    print("\nYet another skeleton down!")
    speep(2)
    print("I am impressed.")
    sleep(1)
    print(f"{blue_text(player.name)}, you are truly skilled.") # type: ignore
    sleep(4)
    print("Though I believe you are skilled, I have not decided whether you are worthy enough for my sword.\n")
    sleep(12)

def third_kill():
    sleep(2)
    print("\nYet another skeleton down!")
    sleep(1)
    print("More worthy opponents shall come.")
    sleep(5)
    print("You are in need of a better weapon.")
    sleep(4)
    print("Thus, I reward you with a sword.\n")
    sleep(5)
    
    player.obtain_item(sword) # type: ignore

    answer = input(f"\nAnything you want to tell {purple_text("Aetherion")}? ")
    if answer == "Aetherion":
        print("You may have noticed that I no longer take pauses in my speech.")
        sleep(2)
        print("This is caused purely by Philip being too lazy to put sleep() statements everywhere.")
        sleep(4)
        print("So me, Martin, fixed it for him.")
        sleep(2)
        print("You're wellcome!")
        sleep(4)
        print(f"Your journey awaits you, {blue_text(player.name)}.\n") # type: ignore
        sleep(12)

    else:
        print("Nothing?")
        sleep(6)
        print("I see.")
        sleep(2)
        print(f"Your journey awaits you, {blue_text(player.name)}.\n") # type: ignore
        sleep(12)

def fourth_kill():
    sleep(2)
    print(f"\n{blue_text(player.name)}, how did you fare in the battle?") # type: ignore
    sleep(4)
    print("Well, we see yet again, so your sword must've done wonders.")
    sleep(6)
    print("Philip is too lazy to make more stages, so in the meantime, enjoy leveling up and killing endless zombies and skeletons!")
    sleep(12)
    print(f"I, {purple_text("Aetherion")} will await our next encounter.")
    sleep(4)
    print("Until then, good luck.\n")
    sleep(10)

title_screen()
initialize_game(player_name)

completed_stage_one = False
completed_stage_two = False
completed_stage_three = False
completed_stage_four = False

while True:
    
    enemies_to_spawn = ["skeleton"]

    if player.murder_count == 1 and not completed_stage_one: # type: ignore
        first_kill()
        completed_stage_one = True

    if player.murder_count == 2 and not completed_stage_two: # type: ignore
        second_kill()
        completed_stage_two = True
    
    if player.murder_count == 3 and not completed_stage_three: # type: ignore
        third_kill()
        enemy_to_spawn = ["zombie"]
        completed_stage_three = True
        
    if player.murder_count == 4 and not completed_stage_four: # type: ignore
        fourth_kill()
        enemy_to_spawn = ["skeleton", "zombie"]
        completed_stage_four = True

    choices = 0

    if "skeleton" in enemies_to_spawn:
        choices += 1

    if "zombie" in enemies_to_spawn:
        choices += 1
    
    if choices == 2:
        if game.randint(0, 1) == 0:
            skeleton = game.Enemy("Skeleton", 50, 0, 10, 20, 50, player.level, 40) # type: ignore
        
        else:
            zombie = game.Enemy("Zombie", 75, 0, 15, 25, 50, player.level, 60) # type: ignore
    
    elif "skeleton" in enemies_to_spawn:
        skeleton = game.Enemy("Skeleton", 50, 0, 10, 20, 50, player.level, 40) # type: ignore
    
    else:
        zombie = game.Enemy("Zombie", 75, 0, 15, 25, 50, player.level, 60) # type: ignore


    player.prompt_attack() # type: ignore

