# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4
# https://isaaccomputerscience.org/concepts/prog_oop_concepts
#
# To run this file you also need to download the file pet_class.py

from pet_class import Pet

def change_pet(my_pet):
    """Allows pet to be changed"""
    answer = input("\nDo you want to change the name of your pet(y/n)? ")
    if answer.lower() == "y":         
        new_name = input("Enter a new name for your pet ")
        my_pet.set_name(new_name)
    answer = input("\nDo you want to change the type of pet you have(y/n)? ")
    if answer.lower() == "y":
        pet_name = my_pet.get_name()
        new_type = input(f"What type of animal is {pet_name}? ")
        my_pet.set_type(new_type)
    answer = input("\nDo you want to change the colour of your pet(y/n)? ")
    if answer.lower() == "y":
        pet_name = my_pet.get_name()
        new_colour = input(f"What colour is {pet_name}? ")
        my_pet.set_colour(new_colour)
    print("\n")
    my_pet.describe()

def show_game_options():
    """Options for game"""
    print ("\n")
    print ("  1. Feed your pet")
    print ("  2. Play with your pet")
    print ("  3. Put your pet to bed")
    print ("  4. Wake your pet up")
    print ("  5. Change pet")
    print ("  9. Finish the game")
    
def main():
    pet_name = input("Enter a name for your pet ")
    pet_type = input(f"What type of animal is {pet_name}? ")
    pet_colour = input(f"What colour is {pet_name}? ")
    my_pet = Pet(pet_name, pet_type, pet_colour) # Makes a pet object
    finished = False
    while finished == False:
        show_game_options()
        choice = input(" What do you want to do? ")
        print("\n")
        if choice == "1":
            my_pet.feed()
        elif choice == "2":
            my_pet.play()
        elif choice == "3":
            my_pet.sleep()
        elif choice == "4":
            my_pet.wake()
        elif choice == "5":
            change_pet(my_pet)
        elif choice == "9":
            finished = True # This will cause game to end
            print ("Thanks for playing the pet game")
        else:
            print("That is not a menu option")    

if __name__ == "__main__":
    main()
