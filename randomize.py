import random


def random_name():
    # names = ["Andrei", "Eron", "Dave", "Zen", "Gilbert", "Marc"]
    names = input("input line of names (separated by space)").split()
    randomInt = random.randint(0, len(names) - 1)
    print(names[randomInt])


choice = input()

match (choice):
    case "names":
        random_name()
    case "exit":
        quit()
    case _:
        print("command not found")
