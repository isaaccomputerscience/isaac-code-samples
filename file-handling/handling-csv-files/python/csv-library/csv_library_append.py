# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

import csv  

def append_record(new_record):
    """Append a record to a CSV file"""
    # Initialise the filename

    filename = "movies_extra.csv";
    
    # Open the file in append mode using the with command
    with open(filename, mode="a") as file_object:
        # Use the csv library to write a new row to the file
        write_to_csv = csv.writer(file_object)
        write_to_csv.writerow(new_record)


def main():
    movie_one = ["The Batman", "2022", "176", "Action,Crime,Drama", "Matt Reeves", "8.3", "350"]
    append_record(movie_one)
    
    movie_two = ["Joker", "2019", "122", "Crime,Drama,Thriller", "Todd Phillips", "8.4", "335.5"]
    append_record(movie_two)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    main()
