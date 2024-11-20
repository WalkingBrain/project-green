import engine as game

player = game.Player("Player", 100, 0, 5, 20, 50, 1, 0)

sword = game.Weapon("Sword", 10, 0, 10, 1, 0)
bow = game.Weapon("Bow", 10, 30, 50, 1, 0)

player.obtain_item(sword)
player.obtain_item(bow)

number = 10

print(number ** 2)

while True:
    if player.experience >= 100:
        player.level += player.experience // 100
        player.experience //= 2
        leveled_up = True

    else:
        leveled_up = False

    if sword.experience >= 100:
        sword.level += sword.experience // 100
        sword.experience //= 2
    
    if bow.experience >= 100:
        bow.level += bow.experience // 100
        bow.experience //= 2

    if not leveled_up:
        skeleton = game.Enemy("Skeleton", 50, 0, 10, 40, 50, player.level, 100)

            
        
    player.prompt_attack()




