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
print("\n")

if skip == "No":
    print("Welcome, traveler.\n")
    sleep(2)
    print(f"{game.blue_text("You")} are lost in a {game.green_text("Dark Forest")}.")
    sleep(4)
    print(f"Oh, yes, {game.purple_text("I")} forgot to introduce {game.purple_text("myself")}.")
    sleep(4)
    print(f"{game.purple_text("I")} am {purple_text("Aetherion")}, the ruler of {game.green_text("Dark Forest")}.")
    sleep(4)
    player_name = input(f"How should I refer to {game.blue_text("you")}? ")
    sleep(1)
    print(f"Yet again, welcome, {game.blue_text(player_name)}.\n")
    sleep(4)
    print(f"{game.blue_text("You")} might be wondering why you're here.")
    sleep(4)
    print("One shall find the reason for struggle after they have defeated it.\n")
    sleep(4)
    print(f"There is a path out, but {game.blue_text("you")} can see a {game.yellow_text("shadowy figure")} ahead.")
    sleep(6)
    print(f"{game.blue_text("You")} identify the shadowy figure as a {game.yellow_text('skeleton')}.\n")
    sleep(4)
    print(f"You wield an old, {game.green_text("rusty sword")}.")
    sleep(4)
    print("It has definitely seen better days, but using it is your only option.")
    sleep(4)
    print(f"{game.blue_text(player_name)}, we shall meet again.")
    sleep(4)
    print("And there, your adventure starts.\n")
    sleep(12)

elif skip == "Yes":
    print(f"{game.blue_text("You")} skippped the dialogue!")
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

    print(f"With that in mind, your first {game.red_text("fight")} shall come along.\n")
    sleep(4)

def first_kill():
    sleep(2)
    print(f"\n{game.blue_text("You")} killed the {game.yellow_text("skeleton")}!")
    sleep(6)
    print(f"Though {game.blue_text("you")} are now a {game.red_text("murderer")}, {game.blue_text("you")} are on the right path.")
    sleep(4)
    print(f"{game.purple_text("I")} shall reward you for your actions later, but for now, you may continue your journey.\n")
    sleep(12)

def second_kill():
    sleep(2)
    print(f"\nYet another {game.yellow_text("skeleton")} down!")
    speep(2)
    print(f"{game.purple_text("I")} am impressed.")
    sleep(1)
    print(f"{game.blue_text(player.name)}, {game.blue_text("you")} are truly skilled.") # type: ignore
    sleep(4)
    print(f"Though {game.purple_text("I")} believe {game.blue_text("you")} are skilled, {game.purple_texdt("I")} have not decided whether {game.blue_text("you")} are worthy enough for my {game.green_text("sword")}.\n")
    sleep(12)

def third_kill():
    sleep(2)
    print(f"\nYet another {game.yellow_text("skeleton") down!")
    sleep(1)
    print(f"More worthy {game.yellow_text("opponents")} shall come.")
    sleep(5)
    print(f"{game.blue_text("You")} are in need of a better {game.green_text("weapon")}.")
    sleep(4)
    print(f"Thus, {game.purple_text("I")} reward {game.blue_text("you")} with a {game.green_text("sword")}.\n")
    sleep(5)
    
    player.obtain_item(sword) # type: ignore

    answer = input(f"\nAnything you want to tell {purple_text("Me")}? ")
    if answer == "Aetherion":
        print(f"{game.blue_text("You")} may have noticed that {game.purple_text("I")} no longer take pauses in my speech.")
        sleep(2)
        print(f"This is caused purely by {game.purple_text("Philip")} being too lazy to put sleep() statements everywhere.")
        sleep(4)
        print(f"So me, {game.purple_text("Martin")}, fixed it for him.")
        sleep(2)
        print(f"{game.blue_text("You")}'re wellcome!")
        sleep(4)
        print(f"Your journey awaits {game.blue_text("you")}, {game.blue_text(player.name)}.\n") # type: ignore
        sleep(12)

    else:
        print("Nothing?")
        sleep(6)
        print(f"{game.purple_text("I")} see.")
        sleep(2)
        print(f"Your journey awaits {game.blue_text("you")}, {game.blue_text(player.name)}.\n") # type: ignore
        sleep(12)

def fourth_kill():
    sleep(2)
    print(f"\n{blue_text(player.name)}, how did {game.blue_text("you")} fare in the battle?") # type: ignore
    sleep(4)
    print("Well, we see yet again, so your sword must've done wonders.")
    sleep(6)
    print(f"{game.purple_text("Philip")} is too lazy to make more stages, so in the meantime, enjoy leveling up and killing endless {game.yellow_text("zombies"}) and {game.yellow_text("skeletons")}!")
    sleep(12)
    print(f"{game.purple_text("I")}, {purple_text("Aetherion")} will await our next encounter.")
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

