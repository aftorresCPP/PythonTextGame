import json
import random



class Character:
    def __init__(self, name, base_health):
        self.name = name                #Names come from the type of soldier below. 
        self.base_health = base_health
   
    def attack(self, weapon, distance_from_player): #3/6/24 I should have done all the coding here, but I didn't. You'll find these completed functions in the soldier classes
                                #Character class is kinda useless the way I have the code set up at the current moment, but I'm still using it
        pass

    def defend(self):
        pass                #I'm going to leave these two empty for now. Not sure if they should be here, or with the specific characters
                            #Technically, all soldiers are charactres, and all can attack or defend. All soldiers have the same base health
    
class HeavySoldier(Character): #Soldiers inherit the attributes and methods of the Character class
    def __init__(self): 
        super().__init__("Heavy Soldier", base_health = 1000) #(name, amout of base health) the soldiers may have different amounts of base health
        
        self.armor_enabled = True #Per the rules of the game, heavies are allowed to use armor. It is a base trait of the class.
        self.shields_enabled = True


        if self.armor_enabled == True: #Base health amount can be changed in the character class because all classes have health. This may not be the best design, but it can be changed later
            self.armor = 500
        else:
            self.armor = 0
        
        if self.shields_enabled == True:
            self.shields = 300
        else:
            self.shields = 0
        



        self.current_health = self.base_health + self.armor + self.shields
        #need something here to make sure heavies are not allowed to use long ranged weapons. Do this later

    def attack(self, weapon, distance_from_player):
        print(f"{self.name} used {weapon['name']}!")  # Access 'name' key in weapon dictionary

        if weapon['range'] >= distance_from_player: #fix this later. This compares the range of the weapon to the distance the target is
            self.current_health -= weapon['healthDMG'] #all characters have base health, so no if statement is needed
            if hasattr(self, 'armor') and self.armor:
                self.current_health -= weapon['armorDMG']
            if hasattr(self, 'shields') and self.shields:
                self.current_health -= weapon['shieldDMG']
        else: 
            print("Out of Range!")
            self.current_health = self.current_health
    
    def defend(self):
        print("defended!")

class LightSoldier(Character): #basically a copy/paste of the character above with their health types enabled. 
    def __init__(self):
        super().__init__("Light Soldier", base_health = 700)
        
        self.armor_enabled = False #Light Soldiers are not allowed armor, but are allowed shields
        self.shields_enabled = True

        
        if self.armor_enabled == True:
            self.armor = 500
        else:
            self.armor = 0
        
        if self.shields_enabled == True:
            self.shields = 300
        else:
            self.shields = 0
        
        self.current_health = self.base_health + self.armor + self.shields

    def attack(self, weapon, distance_from_player):
        print(f"{self.name} used {weapon['name']}!")  # Access 'name' key in weapon dictionary

        if weapon['range'] >= distance_from_player: #fix this later. This compares the range of the weapon to the distance the target is
            self.current_health -= weapon['healthDMG'] #all characters have base health, so no if statement is needed
            if hasattr(self, 'armor') and self.armor:
                self.current_health -= weapon['armorDMG']
            if hasattr(self, 'shields') and self.shields:
                self.current_health -= weapon['shieldDMG']
        else: 
            print("Out of Range!")
            self.current_health = self.current_health
    
    def defend(self):
        print("defended!")

class MeleeSoldier(Character):
    def __init__(self):
        super().__init__("Melee Soldier", base_health = 900)

        self.armor_enabled = False
        self.shields_enabled = False

        
        if self.armor_enabled == True: #This was for a future feature. It may go unused after all to keeo things simple
            self.armor = 500
        else:
            self.armor = 0
        
        if self.shields_enabled == True:
            self.shields = 300
        else:
            self.shields = 0

        self.current_health = self.base_health + self.armor + self.shields
    
    def attack(self, weapon, distance_from_player):
        print(f" {self.name} closes in for an attack!")
        print(f"{self.name} used {weapon['name']}!")  # Access 'name' key in weapon dictionary

        if weapon['range'] >= distance_from_player: 
            self.current_health -= weapon['healthDMG'] #all characters have base health, so no if statement is needed
            if hasattr(self, 'armor') and self.armor:
                self.current_health -= weapon['armorDMG']
            if hasattr(self, 'shields') and self.shields:
                self.current_health -= weapon['shieldDMG']
        else: 
            print("Out of Range!")
            self.current_health = self.current_health
    

class Weapon:
    def __init__(self, name, range, healthDMG, armorDMG, shieldDMG): #weapons and their damage types will come from a json later. weapons can do different types of damage

        self.name = name
        self.range = range
        self.healthDMG = healthDMG
        self.armorDMG = armorDMG
        self.shieldDMG = shieldDMG

#-------------------------------------------------------------------------- General game functions to be called in main()
class Round:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer
        self.distance_from_player = random.randint(1,100) #When the player encounters a new foe, their distance away is randomized from 1-100 "meters"
    
    def start_round(self):
        print(f"A {self.computer} approaches at " + str(self.distance_from_player) + " meters!")
        #print(f"A {self.computer} approaches at " + {self.distance_from_player} + " meters!")
    
    def end_round(self):
        print(f"Player's current health: {self.player.current_health}")
        print(f"Computer's current health: {self.computer.current_health}")

class Game:
    def __init__(self):
        self.player = None  #Playr, computer, and roud are initiliazed to "None". They'll be filled in as the game is started
        self.computer = None
        self.round = None

    def start_game(self):
        self.choose_character()
        self.round = Round(self.player, self.computer)
        self.round.start_round()

    def choose_character(self):
        print("Choose your character:")
        print("1. Heavy Soldier")
        print("2. Light Soldier")
        print("3. Melee Soldier")
        choice = input() #might want to add some exceptions late to prevent this from breaking
        if choice == "1":
            self.player = HeavySoldier()
        elif choice == "2":
            self.player = LightSoldier()
        elif choice == "3":
            self.player = MeleeSoldier()
        
        self.computer = random.choice([HeavySoldier(), LightSoldier(), MeleeSoldier()]) #computer's character is randomized
    
    def load_weapons(self):
         #input(str("Choose filename"))   this was here for debugging to make sure the file can be located and opened
         with open("weapons.json", 'r') as weapon_list:
            self.weapons = json.load(weapon_list)['weapons']

        
         with open("melee_weapons.json", 'r') as weapon_list:
            self.melee_weapons = json.load(weapon_list)['melee_weapons']
    
    def choose_weapon(self):
        if type(self.player) in [HeavySoldier, LightSoldier]:
            print("Choose your weapon:")   
            #print("condition test")     
            for i, weapon in enumerate(self.weapons, 1): 
                print(f"{i}. {weapon['name']} ({weapon['range']})")
            choice = int(input()) - 1 #remember indexing!! hence "-1"
            return self.weapons[choice]
        
        elif type(self.player) in [MeleeSoldier]:
            print("Choose Melee Weapon:")
            for i, weapon in enumerate(self.melee_weapons, 1):
                print(f"{i}. {weapon['name']} ({weapon['range']})")
            choice = int(input()) - 1 #remember indexing!! hence "-1"
            return self.melee_weapons[choice]

    
    def play_round(self):
        player_weapon = self.choose_weapon()

        if type(self.computer) in [HeavySoldier, LightSoldier]:
            computer_weapon = random.choice(self.weapons)

        elif type(self.computer) in [MeleeSoldier]:
            computer_weapon = random.choice(self.melee_weapons)

    #in order for the attack methood to work in the Soldier classes above, weapon and distance_from_player must be passed into attack

        self.player.attack(player_weapon, self.round.distance_from_player)
        print(f"Computer's current health: {self.computer.current_health}")
        print("\n")
        

        print(f"computer used {computer_weapon}")
        self.computer.attack(computer_weapon, self.round.distance_from_player) #Keep this here. it's important for determining if damage is being applied correctly
        print(f"Player's current health: {self.player.current_health}")
        print("\n")
        

        if self.player.current_health <= 0:
            print("You lost!")
            self.end_game() #End game isn't a method right now. Will include this later. I think it's end_roud as of now
        elif self.computer.current_health <= 0:
            print("You won!")
            self.end_game()
        else:
            self.play_round() # I can change ths end condition later


#---------------------------------------------------------------^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# remeber to test calling all the functions and classes here to run the game 
def main():
    testgame = Game() #creating a game instance
    testgame.load_weapons()
    testgame.start_game() #using the start game function in Game(). Enables the character select screen  
    testgame.play_round()

 #2/26/24 testing the combat loop to check for failures. Weapons list can be updated at a later time. See weapons.json file for the format
#!!!!!!!CHECK THE DIRECTORY FOR weapons.json if an error is encountered while opening. I do not have a "try" feature or exceptions 
        #if the file fails to open^
#There is no function to check if the computer is within the range of the player's weapon. I'll add it to attack later (resolved)
    

#BIGNOTE HERE: I finally realized where attribites should be in UML diagrams. In this program, i made ths mistake of repeting functions that ended up being common to the soldier classes
    #I should have put those functions in Character class^^^^
if __name__ == "__main__":
    main()
       


