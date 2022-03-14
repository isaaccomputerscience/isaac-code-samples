# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

import csv 

def read_csv():
   """Read and display the records from a CSV file"""
   filename = "playlist.csv"
   with open(filename, mode="r") as playlist:
       csv_reader = csv.reader(playlist, delimiter=",")
       count = 0
       for line in csv_reader:
          if count == 0:  # Process header record
              print(f"Header: {line[0]}, {line[1]}, {line[2]}")
          else:  # Process data record
              print(f"Data: {line[0]}, {line[1]}, {line[2]}")
          count = count + 1


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    read_csv()
