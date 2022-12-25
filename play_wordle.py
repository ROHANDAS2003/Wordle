from wordle import Wordle

def main():
    print("Hello world!!!")
    wordle = Wordle("APPLE")

    while wordle.can_attempt:
        x = input("Type our guess:  ")
        wordle.attempt(x.upper())
        
    if Wordle.is_solved:
        print("You've guessed it right!!!")
    else:
        print("Wrong guess.")

if __name__ == "__main__":
    main()