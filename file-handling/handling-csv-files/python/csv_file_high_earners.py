# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4


def select_high_earners():
    """Select and display high earning movies"""
    high_earners = 0
    file_object = open("movies.csv", mode="r")
    for record in file_object:
        movie_data = record.split(",")
        revenue = float(movie_data[5])
        
        # Check if the movie revenue was over $200 million
        if revenue > 200: 
            title = movie_data[0]    
            print(f"Movie name: {title}, Revenue: ${revenue} million")
            high_earners = high_earners + 1
    file_object.close()    
    print(f"There were {high_earners} high earning movies.")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    select_high_earners()
