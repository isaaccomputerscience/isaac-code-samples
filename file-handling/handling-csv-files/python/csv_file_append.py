# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


def append_movie():
    """Append a new record to the CSV file"""
    new_movie = "CODA,2021,111,Sian Heder,8.1,1.5"
    file_object = open("movies.csv", mode="a")
    file_object.write(new_movie)
    file_object.write("\n")
    file_object.close()


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    append_movie()
