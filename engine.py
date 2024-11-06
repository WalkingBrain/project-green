import random

class Entity:

    instances = []
    instance_names = {}

    def __init__(self, name, hp,  defense):
        self.name = name
        self.hp = hp
        self.defense = defense
        Entity.instances.append(self)
        Entity.instance_names[self.name.lower()] = self
    
    def take_damage(self, damage):
        self.hp -= damage

    def heal(self, amount):
        self.hp += amount

    def talk(self, words):
        print(f"{self.name}: {words}")
    

class Enemy(Entity):
    
    def __init__(self, name, hp, defense, attack, crit_rate, crit_damage):
        super().__init__(name, hp, defense)
        self.attack = attack
        self.crit_rate = crit_rate
        self.crit_damage = crit_damage
    
    def action_attack(self, target, weapon):
        if self.hp > 0:
            weapon.attack_weapon(target, self)
    
    def say_info(self):
        print(f"{self.name} has {self.hp} hp, {self.defense} defense and {self.attack} attack")


class Weapon:
    """Class for weapons

    Attributes:
        name (str): The name of the weapon
        damage (int): The damage of the weapon
        crit_rate (float): The critical rate of the weapon, in percentage (0 - 100, over 100 = chance to crit multiple times)
        crit_damage (float): The critical damage of the weapon (increases damage by a certain percentage on a crit)
    """    

    instances = {}

    def __init__(self, name, damage, crit_rate, crit_damage):
        self.name = name
        self.damage = damage
        self.crit_rate = crit_rate
        self.crit_damage = crit_damage
        Weapon.instances[self.name] = self
    
    def attack_weapon(self, target, user):

        target = Entity.instance_names[target.lower()]
        

        target.take_damage(self.calculate_damage(target, user))
        if target.hp <= 0:
            print(f"{target.name} died")
        else:
            print(f"{user.name} hit {target.name} with {self.name} for {self.damage+user.attack} damage.")
            print(f"{target.name} has {target.hp} hp left.")

    def calculate_damage(self, target, user):
        local_crit_rate = self.crit_rate + user.crit_rate
        local_crit_damage = self.crit_damage + user.crit_damage

        full_criticals = local_crit_rate // 100
        full_criticals += 1 if random.randint(0, 100) < local_crit_rate % 100 else 0

        damage = (1 - target.defense / (target.defense + 100)) * (self.damage + user.attack) * (1 + full_criticals * local_crit_damage / 100)

        return damage

# NPC class
class NPC(Entity):
    def greet(self):
        print(f"Hello, my name is {self.name}")

# Player class
class Player(Enemy):
    def __init__(self, name, hp, defense, attack, crit_rate, crit_damage):
        # Create an empty inventory list
        inventory = []

        # Assign the inventory list to self.inventory attribute
        self.inventory = inventory

        # Call the parent class __init__ method to initialize name, hp, defense, and attack attributes
        super().__init__(name, hp, defense, attack, crit_rate, crit_damage)
    
    def obtain_item(self, item):
        # Add item to the inventory
        self.inventory.append(item.name)
        print(f"{self.name} has obtained {item.name}")
    
    def drop_item(self, item):
        # Remove item from the inventory
        self.inventory.remove(item.name)
        print(f"{self.name} has dropped {item.name}")
    
    def list_inventory(self):
        # Check if the inventory is empty
        if len(self.inventory) == 0:
            print("Inventory is empty")
        # Print the inventory
        print("Inventory:")
        # Loop through the inventory
        for item in self.inventory:
            print(f"- {Weapon.instances[item].name}\n  Damage: {Weapon.instances[item].damage}")

    def prompt_attack(self):
        """Prompt the player to enter the enemy they want to attack.

        This function will loop until the player enters a valid target.
        If the player enters "exit", the function will exit the game.
        If the player enters "flee", the function will return to the main menu.
        """
        print("Enemies:")
        for enemy in Enemy.instances: # Loop through the list of enemies
            print(f"{enemy.name}:")
            print(f"{enemy.hp} hp, {enemy.defense} defense and {enemy.attack} attack")
        
        choice = input("Enter the enemy you want to attack (exit to exit, flee to go back): ")
        if choice.lower() == "exit": # If the player enters "exit", exit the game
            exit()

        elif choice.lower() == "flee": # If the player enters "flee", return to the main menu
            return

        elif choice.lower() == self.name.lower():
            suicidal_decision = input("You shouldn't attack yourself, are you sure? Yes/No: ")

            if suicidal_decision.lower() == "yes": # Asks the player whether suicide is their choice
                self.ask_weapon(self.name)
            
            else:
                self.prompt_attack()
            
        else:
            if any(instance.name.lower() == choice.lower() for instance in Enemy.instances):
                print("You have entered a valid target. Good job.")
                self.ask_weapon(choice)
            else:
                print("Enter a valid target.")
          

    def ask_weapon(self, target):
        
        self.list_inventory()
        
        choice = input("Enter the weapon you want to use (exit to quit the game, flee to go back): ")
        if choice.lower() == "exit":
            exit()
        elif choice in self.inventory:
            weapon = Weapon.instances[choice]
            weapon.attack_weapon(target, self)
        elif choice.lower() == "flee":
            self.prompt_attack()
        else:
            print("You don't have that item")
            self.ask_weapon(target)
