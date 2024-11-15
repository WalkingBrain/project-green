import engine as game

player = game.Player("Player", 100, 0, 5, 20, 50, 1, 0)

sword = game.Weapon("Sword", 10, 0, 10, 1, 0)
bow = game.Weapon("Bow", 10, 30, 50, 1, 0)

player.obtain_item(sword)
player.obtain_item(bow)




    



    
