# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4
     

def read_file():
    """Read and display all records from a file"""
    with open("playlist.txt", mode = "r") as playlist:
        for track in playlist:
            print(track)   
    

if __name__ == "__main__":
    read_file()

    
