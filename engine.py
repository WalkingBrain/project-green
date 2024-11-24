from random import randint

def red_text(string):
    return f"\033[31m{string}\033[0m"  # ANSI escape code for red text

def blue_text(string):
    return f"\033[34m{string}\033[0m"  # ANSI escape code for blue text

def green_text(string):
    return f"\033[32m{string}\033[0m"  # ANSI escape code for green text

def yellow_text(string):
    return f"\033[33m{string}\033[0m"  # ANSI escape code for yellow text

def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


class Entity:

    instances = []
    instance_names = {}

    def __init__(self, name, hp,  defense):
        self.name = name
        self.max_hp = hp
        self.defense = defense
        self.hp = self.max_hp
        self.is_alive = True

        Entity.instances.append(self)
        Entity.instance_names[self.name.lower()] = self
    
    def take_damage(self, damage):
        self.hp -= damage

    def heal(self, amount):
        self.hp = min(self.hp + amount, self.max_hp)
        print(f"{blue_text(self.name)} has been healed for {green_text(amount)} hp.")

    def talk(self, words):
        print(f"{green_text(self.name)} says: {words}")
    

class Enemy(Entity):
    
    def __init__(self, name, hp, defense, attack, crit_rate, crit_damage, level, experience_worth):

        self.level = level

        constant_multiplier = self.calculate_constant_multiplier()

        super().__init__(name, hp * constant_multiplier, defense * constant_multiplier)

        self.attack = attack * constant_multiplier
        self.crit_rate = crit_rate * constant_multiplier
        self.crit_damage = crit_damage * constant_multiplier
        self.experience_worth = experience_worth


    def action_attack(self, target, weapon):
        if weapon is None:
            bare_hands.attack_weapon(target, self)

        else:
            weapon.attack_weapon(target, self)
    
    def say_info(self):
        print(f"{yellow_text(self.name)} has {red_text(self.hp)} hp, {red_text(self.defense)} defense and {red_text(self.attack)} attack")
        print(f"Also, {yellow_text(self.name)} is level {red_text(self.level)} and has {red_text(self.crit_rate)} crit rate and {red_text(self.crit_damage)} crit damage.")

    def calculate_constant_multiplier(self):
        return 0.99 + self.level / 100


class Weapon:
    """Class for weapons

    Attributes:
        name (str): The name of the weapon
        damage (int): The damage stat of the weapon
        crit_rate (float): The critical rate of the weapon, in percentage (over 100 = chance to crit multiple times)
        crit_damage (float): The critical damage stat of the weapon (increases damage by a certain percentage on a crit)
    """    

    instances = {}

    def __init__(self, name, damage, crit_rate, crit_damage, level, experience, experience_per_level):

        self.level = level
        constant_multiplier = self.calculate_constant_multiplier()

        self.name = name

        self.damage = damage * constant_multiplier
        self.crit_rate = crit_rate * constant_multiplier
        self.crit_damage = crit_damage * constant_multiplier
        self.experience_per_level = experience_per_level * constant_multiplier
        self.experience = experience

        Weapon.instances[self.name.lower()] = self
    
    def attack_weapon(self, target, user):
        calculated_damage, did_crit = self.calculate_damage(target, user)
        target.take_damage(calculated_damage)
        formed_string = f"{blue_text(user.name)} hit {yellow_text(target.name)} with {blue_text(self.name)} for {red_text(calculated_damage)} damage."

        if did_crit:
            formed_string += " Your hit was a critical hit!"

        if target.hp <= 0:
            print(formed_string)
            if isinstance(target, Player):
                print(red_text("You died."))
                target.print_end_stats()
                exit("Successful exit.")

            else:
                print(f"{yellow_text(target.name)} died.")
                user.experience += target.experience_worth
                self.experience += target.experience_worth
                print(f"You have gained {green_text(target.experience_worth)} experience.")
                user.level_up()
                self.level_up()
                user.murder_count += 1
                user.heal((target.max_hp + user.max_hp) / 2)

            target.is_alive = False
            
        else:
            print(formed_string)
            print(f"{yellow_text(target.name)} has {red_text(target.hp)} hp left.")

            if isinstance(target, Enemy) and not isinstance(target, Player):
                target.action_attack(user, None)


    def calculate_damage(self, target, user):
        
        critical_hits = self.calculate_critical_hits(user)
        local_crit_damage = self.crit_damage + user.crit_damage

        local_attack = self.damage + user.attack
        defense_multiplier = 1 - target.defense / (target.defense + 100)
        critical_hit_multiplier = 1 + critical_hits * local_crit_damage / 100

        damage = defense_multiplier * local_attack * critical_hit_multiplier
        did_crit = True if critical_hits else False

        return damage, did_crit
    
    def calculate_critical_hits(self, user):
        local_crit_rate = self.crit_rate + user.crit_rate

        critical_hits = local_crit_rate // 100
        critical_hits  += 1 if randint(0, 100) < local_crit_rate % 100 else 0

        return critical_hits
    
    def calculate_constant_multiplier(self):
        return 0.99 + self.level / 100

    def level_up(self):
        while self.experience >= self.experience_per_level:
            self.experience -= self.experience_per_level
            self.recalculate_stats_on_level_up()

    def recalculate_stats_on_level_up(self):
        
        constant_multiplier = self.calculate_constant_multiplier()

        self.damage /= constant_multiplier
        self.crit_rate /= constant_multiplier
        self.crit_damage /= constant_multiplier
        self.experience_per_level /= constant_multiplier

        self.level += 1
        print(f"{blue_text(self.name)} has leveled up to level {blue_text(self.level)}!")

        constant_multiplier = self.calculate_constant_multiplier()

        self.damage *= constant_multiplier
        self.crit_rate *= constant_multiplier
        self.crit_damage *= constant_multiplier
        self.experience_per_level *= constant_multiplier



# NPC class
class NPC(Entity):
    def greet(self):
        print(f"Hello, my name is {self.name}")

# Player class
class Player(Enemy):
    def __init__(self, name, hp, defense, attack, crit_rate, crit_damage, level, experience, experience_per_level):

        self.inventory = []

        self.experience = experience
        self.experience_per_level = experience_per_level
        self.murder_count = 0

        super().__init__(name, hp, defense, attack, crit_rate, crit_damage, level, 0)
    
    def obtain_item(self, item):
        # Add item to the inventory
        self.inventory.append(item.name.lower())
        print(f"{blue_text(self.name)} has obtained {green_text(item.name)}")
    
    def drop_item(self, item):
        # Remove item from the inventory
        self.inventory.remove(item.name.lower())
        print(f"{blue_text(self.name)} has dropped {green_text(item.name)}")
    
    def list_inventory(self):
        print("Inventory:")
        index = 0
        for item in self.inventory:
            index += 1
            weapon = Weapon.instances[item]
            print(f"- {green_text(weapon.name)} ({green_text(index)}):")
            print(f"    Level: {blue_text(weapon.level)}")
            print(f"    Damage: {red_text(weapon.damage)}")
            print(f"    Crit Rate: {red_text(weapon.crit_rate)}")
            print(f"    Crit Damage: {red_text(weapon.crit_damage)}")
            print(f"    Experience: {red_text(weapon.experience)}")
            print(f"    Experience until next level: {red_text(weapon.experience_per_level - weapon.experience)}\n")

    def prompt_attack(self):
        """Prompt the player to enter the enemy they want to attack.

        This function will loop until the player enters a valid target.
        If the player enters "exit", the function will exit the game.    Crit Damage: {Weapon.instances[item].crit_damage}
        If the player enters "flee", the function will return to the main menu.
        """
        valid_enemies = [enemy for enemy in Enemy.instances if enemy.is_alive and not isinstance(enemy, NPC)]
        print("Your enemies are:")
        index = 0
        for enemy in valid_enemies: # Loop through the list of enemies
            index += 1
            print(f"{yellow_text(enemy.name)} ({green_text(index)}):")
            print(f"{red_text(enemy.hp)} out of {red_text(enemy.max_hp)} hp, {red_text(enemy.defense)} defense and {red_text(enemy.attack)} attack")
        
        choice = input("Enter the enemy you want to attack (exit to exit) ")
        if choice.lower() == "exit": # If the player enters "exit", exit the game
            exit()

        elif choice.lower() == self.name.lower() or (int(choice) == 1 if is_int(choice) else 0):
            suicidal_decision = input(f"You shouldn't attack yourself, are you sure? {red_text('Yes')}/{green_text('No')}: ")

            if suicidal_decision.lower() == "yes": # Asks the player whether suicide is their choice
                print(f"{yellow_text("You asked for this.")} Results may include death or serious injuries.")
                self.ask_weapon(self)
            
            else:
                self.prompt_attack()

        elif is_int(choice) and int(choice) <= len(valid_enemies):

            choice = valid_enemies[int(choice) - 1]

            print(f"You have entered a valid target. {green_text('Good job.')}")
            self.ask_weapon(choice)

            
        else:
            if any(instance.name.lower() == choice.lower() for instance in valid_enemies):
                print(f"You have entered a valid target. {green_text("Good job.")}")
                choice = Enemy.instance_names[choice.lower()]
                self.ask_weapon(choice)

            else:
                print(red_text("\nEnter a valid target.\n"))
          

    def ask_weapon(self, target):
        
        self.list_inventory()
        
        choice = input("Enter the weapon you want to use (exit to quit the game, flee to go back): ")
        if choice.lower() == "exit":
            exit()

        elif is_int(choice):
            if int(choice) <= len(self.inventory):
                weapon = Weapon.instances[self.inventory[int(choice) - 1]]
                weapon.attack_weapon(target, self)

        elif choice.lower() in self.inventory:
            weapon = Weapon.instances[choice.lower()]
            weapon.attack_weapon(target, self)

        elif choice.lower() == "flee":
            self.prompt_attack()

        else:
            print("You don't have that item")
            self.ask_weapon(target)

    def level_up(self):
        while self.experience >= self.experience_per_level:
            self.experience -= self.experience_per_level
            self.recalculate_stats_on_level_up()

    def recalculate_stats_on_level_up(self):
        
        constant_multiplier = self.calculate_constant_multiplier()

        self.max_hp /= constant_multiplier
        self.hp /= constant_multiplier
        self.defense /= constant_multiplier
        self.attack /= constant_multiplier
        self.crit_rate /= constant_multiplier
        self.crit_damage /= constant_multiplier
        self.experience_per_level /= constant_multiplier

        self.level += 1
        print(f"{blue_text(self.name)} has leveled up to level {blue_text(self.level)}!")

        constant_multiplier = self.calculate_constant_multiplier()

        self.max_hp *= constant_multiplier
        self.hp *= constant_multiplier
        self.defense *= constant_multiplier
        self.attack *= constant_multiplier
        self.crit_rate *= constant_multiplier
        self.crit_damage *= constant_multiplier
        self.experience_per_level *= constant_multiplier

    def print_end_stats(self):
        print(f"You managed to get a whopping {blue_text(self.level)} {"level" if self.level == 1 else "levels"}.")
        print(f"You have also gained {yellow_text(self.experience)} experience {"point" if self.experience == 1 else "points"}.")
        print(f"You would need {yellow_text(self.experience_per_level - self.experience)} {"point" if self.experience_per_level - self.experience == 1 else "points"} to level up again.")
        print("Good job")

# Definitions of engine-crucial instances
bare_hands = Weapon("Bare hands", 5, 10, 20, 1, 0, 60)

# Test the functions
if __name__ == "__main__":
    print(red_text("This is red text"))
    print(blue_text("This is blue text"))
    print(green_text("This is green text"))
    print(yellow_text("This is yellow text"))