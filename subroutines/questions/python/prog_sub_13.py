def badger():
    """Prints the word Badger"""
    print("Badger")

def mushroom():
    """Prints the word Mushroom"""
    print("Mushroom")


def song():
    """Prints the words of a delightful song"""
    for i in range(12):
        badger()
    mushroom()
    mushroom()

if __name__ == '__main__':
    song()
