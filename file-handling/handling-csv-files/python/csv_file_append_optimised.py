# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


def append_movie_optimised(title, year, duration, director, rating, takings):
    """Optimised version to append a new record to the CSV file"""
    new_film = title + "," + year + "," + duration + "," + director + "," + rating + "," + takings
    with open("movies.csv", mode="a") as file_object:
        file_object.write(new_film)
        file_object.write("\n")


def main():
    title = input("Enter the title of the film: ")
    year = input("Enter the year the film was made: ")
    duration = input("Enter the length of the film in minutes: ")
    director = input("Enter the name of the film director: ")
    rating = input("Enter the average film rating: ")
    takings = input("Enter the takings in US$ millions: ")
    append_movie_optimised(title, year, duration, director, rating, takings)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    main()
