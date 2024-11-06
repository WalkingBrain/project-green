import engine as game

player = game.Player("Player", 10, 1, 5, 0, 100)
target_dummy = game.Entity("Dummy", 10, 100)

sword = game.Weapon("Sword", 5, 200, 0)
player.obtain_item(sword)

print(f"{sword.name} deals {sword.calculate_damage(target_dummy, player)} damage")
