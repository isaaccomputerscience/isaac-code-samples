# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

import csv

def read_csv():
   with open("myplaylist.csv", mode = "r") as file:
       csvfile = csv.reader(file)
       for line in csvfile:
           print(line)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    read_csv()
