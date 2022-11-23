# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

def rent_check():
    """Example of nested selection to check user can rent a flat"""
    input_age = input("Enter your age: ")
    age = int(input_age)    
   
    if age >= 21:
        input_salary = input("Enter your salary: ")
        salary = int(input_salary)
        
        if salary > 15000:
            print("You can rent the flat")
        else:
            print("You don't earn enough to rent the flat")
    elif age >= 18 and age < 21:
        guarantor = input("Do you have a guarantor (yes/no): ")
        
        if guarantor == "yes":
            print("We will need to contact your guarantor")
        else:
            print("I am sorry but you need a guarantor")
    else:
        print("I am sorry but you can't rent the flat")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    rent_check()
