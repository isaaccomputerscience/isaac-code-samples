def badger():
    print("Badger")

def mushroom():
    print("Mushroom")


def song():
    for i in range(12):
        badger()
    mushroom()
    mushroom()

if __name__ == '__main__':
    song()