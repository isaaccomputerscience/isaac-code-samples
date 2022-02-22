# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

import csv  

def write_csv():
    header = ["Artist", "Song title", "Duration"]
    track_one = ["Pharrell Williams", "Happy", "03:55"]
    track_two = ["Meat Loaf", "Bat out of hell", "09:50"]
    track_three = ["Adele", "Easy on me", "03:44"]
    track_four = ["Elton John & Dua Lipa", "Cold heart", "03:22"]

    with open("myplaylist.csv", "w") as file:
        write_to_csv = csv.writer(file)
        write_to_csv.writerow(header)
        write_to_csv.writerow(track_one)
        write_to_csv.writerow(track_two)
        write_to_csv.writerow(track_three)
        write_to_csv.writerow(track_four)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    write_csv()
