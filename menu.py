def menu(*args):
    while True:
        choice = input("Enter your choice: ")
        if choice in args:
            return choice
