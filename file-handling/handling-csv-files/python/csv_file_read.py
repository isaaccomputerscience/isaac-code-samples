# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

import csv

def read_csv():
   filename = "playlist.csv"
   with open(filename, mode = "r") as playlist:
       playlist = csv.reader(playlist)
       for line in playlist:
           print(line)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    read_csv()
