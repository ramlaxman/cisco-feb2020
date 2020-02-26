def menu(*args):
    while True:
        choice = input(f"Enter your choice {args}: ")
        if choice in args:
            return choice
        print(f'Bad choice of {choice}!  Try again.')
