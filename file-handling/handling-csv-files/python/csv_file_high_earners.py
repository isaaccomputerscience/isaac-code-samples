# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def select_high_earners():
    """Select and display high earning movies"""
    record_num = 0
    high_earners = 0
    
    file_object = open("movies.csv", mode="r")
    for record in file_object:
        # Ignore the header row
        if record_num != 0:
            movie_data = record.split(",")
            revenue = float(movie_data[5])
            
            # Check if the movie revenue was over $200 million
            if revenue > 200: 
                title = movie_data[0]    
                print(f"Film name: {title}, Revenue: {revenue}")
                high_earners = high_earners + 1
        record_num = record_num + 1
    file_object.close()    
    print(f"There were {high_earners} high earning movies.")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    select_high_earners()
