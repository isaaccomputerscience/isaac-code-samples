# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

import csv  

def append_csv():
    filename = "playlist.csv"
    new_track = ["Jorja Smith", "Addicted", "03:24"]
    with open(filename, mode = "a") as playlist:
        write_to_csv = csv.writer(playlist)
        write_to_csv.writerow(new_track)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    append_csv()
