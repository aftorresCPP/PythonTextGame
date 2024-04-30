import json
import random
import os

class Character:
    def __init__(self, name, base_health):
        self.name = name
        self.base_health = base_health
        self.is_dodge = False
        self.score = 0

    def attack(self, weapon, opponent, distance_from_player):
        
        #print(f"{self.name} used {weapon['name']}!")  

        #if weapon['ammo'] > 0 :
        if 'ammo' in weapon and weapon['ammo'] > 0: # this line is a temporary fix, not sure if it works all the time

            if weapon['range'] >= distance_from_player: 
                opponent.current_health -= weapon['healthDMG']  
                if hasattr(self, 'armor') and self.armor:
                    opponent.current_health -= weapon['armorDMG']
                if hasattr(self, 'shields') and self.shields:
                    opponent.current_health -= weapon['shieldDMG']

                #weapon['ammo']-=1
                print(f"{self.name} used {weapon['name']}!")
            else: 
                print(f"{self.name} used {weapon['name']}!")
                print("Out of Range!")
                self.current_health = self.current_health
            weapon['ammo']-=1

        else:
            #print("This weapon is out of ammo! Choose another weapon!")
            return False
        return True
    

    

    
    """def attack(self, weapon, opponent, distance_from_player):
        
        print(f"{self.name} used {weapon['name']}!")  # Access 'name' key in weapon dictionary
    
    
        if  > 0:
            if weapon['range'] >= distance_from_player: 
                opponent.current_health -= weapon['healthDMG']  
                if hasattr(self, 'armor') and self.armor:
                    opponent.current_health -= weapon['armorDMG']
                if hasattr(self, 'shields') and self.shields:
                        opponent.current_health -= weapon['shieldDMG']
            else: 
                print("Out of Range!")
                self.current_health = self.current_health
        else:
            print("choose another weapon!")"""


    def defend(self):
        print(f"{self.name} dodged the attack!")
        self.is_dodge = True


class HeavySoldier(Character):
    def __init__(self): 
        super().__init__("Heavy Soldier", base_health=1000)
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


class LightSoldier(Character): #basically a copy/paste of the character above with their health types enabled. 
    def __init__(self):
        super().__init__("Light Soldier", base_health = 900)
        
        self.armor_enabled = False #Light Soldiers are not allowed armor, but are allowed shields
        self.shields_enabled = True
        if self.armor_enabled == True:
            self.armor = 500
        else:
            self.armor = 0
        if self.shields_enabled == True:
            self.shields = 800
        else:
            self.shields = 0
        
        self.current_health = self.base_health + self.armor + self.shields


class MeleeSoldier(Character):
    def __init__(self):
        super().__init__("Melee Soldier", base_health = 700)
        self.armor_enabled = False
        self.shields_enabled = False
        if self.armor_enabled == True: #This was for a future feature. It may go unused after all to keeo things simple
            self.armor = 800
        else:
            self.armor = 0
        if self.shields_enabled == True:
            self.shields = 300
        else:
            self.shields = 0

        self.current_health = self.base_health + self.armor + self.shields

class Turn:
    def __init__(self, player, computer, weapons, melee_weapons):
        self.player = player
        self.computer = computer
        self.weapons = weapons
        self.melee_weapons = melee_weapons
        self.distance_from_player = random.randint(1,500) #When the player encounters a new foe, their distance away is randomized from 1-500 "meters"
    
    def open_weapon_bag(self):
        selected_weapons_options = []

        if type(self.player) in [HeavySoldier, LightSoldier]:
            for i, weapon in enumerate(self.weapons, 1): 
                print(f"{i}. {weapon['name']} --- {weapon['Description']} Stats--- Range:{weapon['range']}, DMG:{weapon['healthDMG']}, Armor DMG: {weapon['armorDMG']}, Sheild DMG:{weapon['shieldDMG']}") #Ammo: {weapon['ammo']}")
            num_choices = 3
            print("Choose three weapons to use on this encounter")
            while num_choices > 0:
                try:
                    choice = int(input("Choose a weapon # from your bag: ")) - 1
                    selected_weapons_options.append(choice)
                    num_choices-=1
                except ValueError:
                    print("That isn't a number. Where did you go to school?")
            selected_weapons = [self.weapons[i] for i in selected_weapons_options]
            return selected_weapons

            """ try:   
                selected_weapons = [self.weapons[i] for i in selected_weapons_options]
                return selected_weapons
            except IndexError:
                    print("We didn't have enough money in the budget to program more than 25 weapons. Try again")
                    self.open_weapon_bag()
            except ValueError:
                    print("That isn't a number. Where did you go to school?")"""
        
        elif type(self.player) in [MeleeSoldier]:
            """for i, weapon in enumerate(self.melee_weapons, 1):
                print(f"{i}. {weapon['name']} ({weapon['range']})")
            num_choices = 3
            print("Choose three weapons to use on this encounter")
            while num_choices > 0:
                choice = int(input("Choose weapon")) - 1
                selected_weapons_options.append(choice)
                num_choices-=1
            selected_weapons = [self.melee_weapons[i] for i in selected_weapons_options]
            return selected_weapons"""
            for i, weapon in enumerate(self.melee_weapons, 1): 
                print(f"{i}. {weapon['name']} --- {weapon['Description']} Stats--- Range:{weapon['range']}, DMG:{weapon['healthDMG']}, Armor DMG: {weapon['armorDMG']}, Sheild DMG:{weapon['shieldDMG']}") #Ammo: {weapon['ammo']}")
            num_choices = 3
            print("Choose three melee weapons to use on this encounter")
            while num_choices > 0:
                try:
                    choice = int(input("Choose a weapon # from your bag: ")) - 1
                    selected_weapons_options.append(choice)
                    num_choices-=1
                except ValueError:
                    print("That isn't a number. Where did you go to school?")
            selected_weapons = [self.melee_weapons[i] for i in selected_weapons_options]
            return selected_weapons


    
    def start_turn(self):
        print(f"An enemy {self.computer.name} approaches at " + str(self.distance_from_player) + " meters!")
        selected_weapons = self.open_weapon_bag()
        self.selected_weapons = selected_weapons
        #print(f"A {self.computer} approaches at " + {self.distance_from_player} + " meters!")
    
    def end_turn(self):
        print(f"Player's current health: {self.player.current_health}")
        print(f"Computer's current health: {self.computer.current_health}")
    
    
    
    

class Game:

    save_file = "saved_game.json" #using this as the default save name with no option to name it

    def __init__(self):
        self.player = None
        self.computer = None
        self.turn = None
        self.load_saved_game = False
        self.loaded_weapons = None
        self.loaded_melee_weapons = None
    


    def start_game(self):
        self.load_weapons()
        if os.path.exists(self.save_file):
            choice = input("Do you wish to contuinue your campaign against the enemy? (Y/N)").upper()
            if choice == "Y":
                self.load_saved_game = True
            else:
                self.load_saved_game = False
        else:
            self.load_saved_game = False

        if self.load_saved_game:
            """self.load_game()  
            self.load_weapons()
            self.turn = Turn(self.player, self.computer, self.loaded_weapons, self.loaded_melee_weapons)
            self.turn.start_turn()"""
            self.load_game()
            self.load_weapons()
        else:
            """self.choose_character()
            self.load_weapons()
            self.turn = Turn(self.player, self.computer, self.loaded_weapons, self.loaded_melee_weapons)
            self.turn.start_turn()"""
            self.choose_character()
            self.load_weapons()
        
        while True:
            self.turn = Turn(self.player, self.computer, self.loaded_weapons, self.loaded_melee_weapons)
            self.turn.start_turn()
            self.play_turn()
            choice  = input("Do you wish to continue your campaign against the enemy?(Y/N)").upper()
            if choice == "Y":
                #self.turn.start_turn() #Needed to add this to make sure that continuing allows the player to re-selct weapons
                self.load_weapons()
                break
    
    
    def load_weapons(self):
        with open("weapons.json", 'r') as weapon_list:
            self.loaded_weapons = json.load(weapon_list)['weapons']

        with open("melee_weapons.json", 'r') as weapon_list:
            self.loaded_melee_weapons = json.load(weapon_list)['melee_weapons']

    def load_game(self):
        print("loading save")
        with open("saved_game.json", 'r') as file:
            data = json.load(file)
            character_type = data.get("character_type", "HeavySoldier") #default save state just in case there are save/load errors
            score = data.get("score", 0) #just realized that save_game() saves the char type without a space. Literally would have saved me two hours or debugging if I realized it sooner
            if character_type == "HeavySoldier":
                self.player = HeavySoldier()
                print("Welcome back Heavy Soldier")
            elif character_type == "LightSoldier":
                self.player = LightSoldier()
                print("Welcome back Light Soldier")
            elif character_type == "MeleeSoldier":
                self.player = MeleeSoldier()
                print("Welcome back Melee Soldier")
            else:
                print("invalid save data. resorting to default chatacter") #temorary fix
                self.player  =HeavySoldier()
            
            
            self.player.score = score
            self.computer = random.choice([HeavySoldier(), LightSoldier(), MeleeSoldier()])
        #print("save loaded")


    def choose_character(self):
        print("Choose your character:")
        print("1. Heavy Soldier")
        print("2. Light Soldier")
        print("3. Melee Soldier")
        choice = int(input())
        try:
            if choice == 1:
                self.player = HeavySoldier()
            elif choice == 2:
                self.player = LightSoldier()
            elif choice == 3:
                self.player = MeleeSoldier()

            self.computer = random.choice([HeavySoldier(), LightSoldier(), MeleeSoldier()])
        except ValueError:
            print("value error")
            self.choose_character()
        except IndexError:
            print("not that either")
            self.choose_character()

    
    def choose_weapon(self):
        action_type = None
        while action_type not in ["A", "D", "Q"]:
            print("What is your course of action?")
            print("Attack (A), Dodge (D), Quit (Q)")
            action_type = input().upper()
            if action_type == "A":
                try:
                    print("Choose your weapon:")   
                    for i, weapon in enumerate(self.turn.selected_weapons, 1): 
                        print(f"{i}. {weapon['name']}, Range:{weapon['range']}, Ammo:{weapon['ammo']}")
                    choice = int(input()) - 1
                    if 0 <= choice < len(self.turn.selected_weapons):
                        return self.turn.selected_weapons[choice]    
                    else:
                        print("Uhh.. can you count? Enter a valid number!")
                except ValueError:
                    print("Uhh.. can you count? Enter a number you idiot!")
                except IndexError:
                    print("Uhh.. can you count? You don't have more than 3 pockets. Those ain't cargo shorts, buddy!")
            elif action_type == "D":
                self.player.defend()
                return None
            elif action_type == "Q":
                self.save_game()
                self.end_game()
    
       

    def play_turn(self):
        action = self.choose_weapon()
        computer_weapon = random.choice(self.loaded_weapons) if type(self.computer) in [HeavySoldier, LightSoldier] else random.choice(self.loaded_melee_weapons)

        if action is not None:
            if not self.player.attack(action, self.computer, self.turn.distance_from_player):
                print("*CLICK CLICK*...This weapon is out of ammo! Choose another weapon.")
            else:
                #computer_weapon = None
                if type(self.computer) in [HeavySoldier, LightSoldier]:
                    computer_weapon = random.choice(self.loaded_weapons)
                    
                elif type(self.computer) in [MeleeSoldier]:
                    computer_weapon = random.choice(self.loaded_melee_weapons)
                    

            #self.player.attack(action,self.computer, self.turn.distance_from_player)
            print(f"Computer's current HP: {self.computer.current_health}")
            
            if computer_weapon:
                #print(f"Computer used {computer_weapon['name']}!")
                self.computer.attack(computer_weapon, self.player, self.turn.distance_from_player)
                print(f"Player's current HP: {self.player.current_health}")

            """#print(f"Computer used {computer_weapon['name']}!")
            self.computer.attack(computer_weapon, self.player, self.turn.distance_from_player)
            print(f"Player's current HP: {self.player.current_health}")
            #print("\n")"""

            if self.player.current_health <= 0:
                print("Warning: Exo Suit Has Been Breached! Oxygen Status: FAIL")
                self.end_game()
            elif self.computer.current_health <= 0:
                print(f"Enemy {self.computer.name} destroyed! ")
                print("Well done... you survived this encounter...")
                self.increase_score()
                print("Opponents slaughtered so far: ", self.player.score)
                self.save_game()
                #self.play_turn()
                self.start_game()
            else:
                self.play_turn()

        elif self.player.is_dodge:
            self.player.is_dodge = False  # the status needs to be reset if the playter chooses to defend

            computer_weapon = random.choice(self.loaded_weapons) if type(self.computer) in [HeavySoldier, LightSoldier] else random.choice(self.loaded_melee_weapons)
            print(f"Computer used {computer_weapon['name']}!, but missed!")
            #self.computer.attack(computer_weapon, self.player, self.turn.distance_from_player)
            print(f"Player's current health: {self.player.current_health}")
            print("\n")
            if self.player.current_health <= 0:
                print("Warning: Exo Suit Has Been Breached! Oxygen Status: FAIL")
                self.end_game()
            elif self.computer.current_health <= 0:
                print(f"Enemy {self.computer.name} destroyed! ")
                print("Well done... you survived this encounter...")
                self.increase_score()
                print("Opponents slaughtered so far: ", self.player.score)
                self.save_game()
                self.start_game()
                
            else:
                self.play_turn()
        

    def end_game(self):
        print("Game Over")

    def increase_score(self):
        self.player.score += 1
    
    def save_game(self):
        print("your progress has been saved")
        data = {"character_type": type(self.player).__name__, "score": self.player.score}
        with open("saved_game.json", 'w') as file:
            json.dump(data, file)
        

def main():
    testgame = Game() #creating a game instance
    testgame.load_weapons()
    testgame.start_game() #using the start game function in Game(). Enables the character select screen  
    testgame.play_turn()

if __name__ == "__main__":
    main()
