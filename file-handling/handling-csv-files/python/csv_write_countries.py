# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

import csv  

def write_csv():
    header = ["Country", "Population", "Continent"]
    nigeria = ["Nigeria", "216746934", "Africa"]
    china = ["China", "1448471400", "Asia"]
    russia = ["Russia", "145805947", "Europe"]
    usa = ["United States", "334805269", "North America"]
    brazil = ["Brazil", "215353593", "South America"]
    australia = ["Australia", "26068792", "Oceania"]

    filename = "playlist.csv"

    with open("countries_population.csv", "w") as countries:
        write_to_csv = csv.writer(countries)
        write_to_csv.writerow(header)
        write_to_csv.writerow(nigeria)
        write_to_csv.writerow(china)
        write_to_csv.writerow(russia)
        write_to_csv.writerow(usa)
        write_to_csv.writerow(brazil)
        write_to_csv.writerow(australia)


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    write_csv()
