# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

import csv  

def write_csv():
    """Write records to a CSV file"""
    header = ["Artist", "Song", "Duration"]
    track_one = ["Pharrell Williams", "Happy", "03:55"]
    track_two = ["Meat Loaf", "Bat out of hell", "09:50"]
    track_three = ["Adele", "Easy on me", "03:44"]
    track_four = ["Olivia Rodrigo", "deja vu", "03:35"]

    filename = "playlist.csv"

    with open(filename, mode="w", newline="") as playlist:
        csv_writer = csv.writer(playlist)
        csv_writer.writerow(header)
        csv_writer.writerow(track_one)
        csv_writer.writerow(track_two)
        csv_writer.writerow(track_three)
        csv_writer.writerow(track_four)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    write_csv()
