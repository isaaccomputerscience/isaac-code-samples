# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

import csv 

def movies_by_genre(genre):
    """Display the records that match a given genre"""
    # Initialise the filename and count
    filename = "movies_extra.csv";
    count = 0
    
    # Capitalise the first letter of each word in genre
    genre = genre.title()

    # Open the file in read mode using the with command
    with open(filename, mode="r") as file_object:
        # Use the csv library to read the file and specify the delimiter
        csv_reader = csv.reader(file_object, delimiter=",")
        for line in csv_reader:
            # Check if the genre is in the genre field
            if genre in line[3]:
                print(f"Data: {line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}, {line[5]}, {line[6]}")
                count = count + 1
    return count


def main():
    genre_chosen = input("Enter a genre of movie to find: ")
    
    total = movies_by_genre(genre_chosen)
    print(f"There were {total} movies containing the genre {genre_chosen}")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    main()
