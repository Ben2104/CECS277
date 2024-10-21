from dragon import *
from entity import *
from fire_dragon import *
from fire import *
from flying_dragon import *
from flying import *
from flying_fire_dragon import *
from hero import *
from check_input import get_int_range
from random import randint

def main():
    
    name = input("What is your name, challenger? \n")
    hero = Hero(name, 50)
    dragons = [FireDragon(), Flying_Dragon(), FlyingFireDragon()]
    print()
    print(f"Welcome to dragon training, {name}")
    print("You must defeat 3 dragons")
    print(hero)
    while dragons:
        print(hero)
        for i, dragon in enumerate(dragons):
                print(f"{i+1}. {dragon}")
        dragon_attack_choice = get_int_range("Choose a dragon to attack: ", 1,len(dragons))
        while(True):
            
            print("1. Sword (2 D6)")
            print("2. Arrow (1 D12)")
                            
            weapon_choice = get_int_range("Enter weapon: ", 1,2)
            if weapon_choice == 1:
                            print(hero.basic_attack(dragons[dragon_attack_choice-1]))
                            dragon_attack = randint(1,2)
                            if dragon_attack == 1:
                                print(dragons[dragon_attack_choice-1].basic_attack(hero))
                            else:
                                print(dragons[dragon_attack_choice-1].special_attack(hero))
            else:
                print(hero.special_attack(dragons[dragon_attack_choice-1]))
                dragon_attack = randint(1,2)
                if dragon_attack == 1:
                    print(dragons[dragon_attack_choice-1].basic_attack(hero))
                else:
                    print(dragons[dragon_attack_choice-1].special_attack(hero))            
                                        
                        
            
            if dragons[dragon_attack_choice-1].hp == 0:
                    dragons.remove(dragons[dragon_attack_choice-1])
                    if not dragons:
                        print("Congratulations! You have defeated all three dragons, you have passed the trials.")
                        break
                    break
            if hero.hp == 0:
                print("You are knocked out, unlucky")
                break
            
            print(hero)    
            for i, dragon in enumerate(dragons):
                            print(f"{i+1}. {dragon}")
                
main()
        
    
    