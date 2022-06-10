# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

def blast_off(n):
    """Count down timer"""

    if n == 0:
        print("Blast off!")
    else:
        print(n)
        blast_off(n-1)

def main():
    blast_off(5)

if __name__ == '__main__':
    main()