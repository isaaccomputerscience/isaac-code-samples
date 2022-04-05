# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


def add_song(title, artist, duration):
    """Append a new song to the playlist"""
    new_song = title + "," + artist + "," + duration
    file_object = open("playlist.csv", mode="a")
    file_object.write(new_song)
    file_object.write("\n")
    file_object.close()


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == "__main__":
    add_song("Happy", "Pharrell Williams", "03:55")
