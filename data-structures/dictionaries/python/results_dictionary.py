# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0


def main():
    """Create a dictionary and perform various actions on it"""

    results = {"Detra": 17,
           "Nova": 84,
           "Charlie": 22,
           "Hwa": 75,
           "Roxann": 92,
           "Elsa": 29}
    
    # Display the score of Charlie
    score = results["Charlie"]
    print(f"Charlie's score is {score}\n")

    # Insert a new key-value pair for Bob
    results["Bob"] = 78
    print(f"Bob has been added with score {results['Bob']}\n")

    # Update the score of Hwa
    results["Hwa"] = 71
    print(f"Hwa's new score is {results['Hwa']}\n")

    # Delete the key-value pair for Elsa
    results.pop("Elsa")
    print("Elsa has been deleted\n")

    # Repeat for each key-value pair in the dictionary
    for key, value in results.items():
        # Output the key-value pair of each item
        print(f"Key: {key}  Value: {value}")


# This code will run if this file is executed directly
# (i.e. not called by another program)
if __name__ == '__main__':
    main()
