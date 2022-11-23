# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4
# https://isaaccomputerscience.org/concepts/prog_oop_concepts

from pet_class import Pet

def main():
    pet_name = input("Enter the name of your pet ")
    pet_type = input(f"What type of animal is {pet_name}? ")
    pet_colour = input(f"What colour is {pet_name}? ")
    my_pet = Pet(pet_name, pet_type, pet_colour)  # Instantiation

    if my_pet.is_sleeping():
        print(f"Shhhhhh, {pet_name} is asleep")
    else:
        print(f"{pet_name} is awake")
   
if __name__ == "__main__":
    main()
