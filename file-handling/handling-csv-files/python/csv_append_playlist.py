# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

import csv  

def append_csv():
    new_track = ["Carolina Gaitán", "We don't talk about Bruno", "03:36"]
    with open("myplaylist.csv", mode = "a") as file:
        write_to_csv = csv.writer(file)
        write_to_csv.writerow(new_track)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    append_csv()
