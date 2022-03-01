# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

import csv  

def write_csv():
    header = ["Artist", "Song", "Duration"]
    track_one = ["Pharrell Williams", "Happy", "03:55"]
    track_two = ["Meat Loaf", "Bat out of hell", "09:50"]
    track_three = ["Adele", "Easy on me", "03:44"]
    track_four = ["Olivia Rodrigo", "deja vu", "03:35"]

    filename = "playlist.csv"

    with open(filename, "w") as playlist:
        write_to_csv = csv.writer(playlist)
        write_to_csv.writerow(header)
        write_to_csv.writerow(track_one)
        write_to_csv.writerow(track_two)
        write_to_csv.writerow(track_three)
        write_to_csv.writerow(track_four)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    write_csv()
