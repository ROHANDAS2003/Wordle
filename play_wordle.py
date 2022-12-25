from wordle import Wordle

def main():
    print("Hello world!!!")
    wordle = Wordle("APPLE")

    while wordle.can_attempt:
        x = input("Type our guess:  ")

        if len(x) != wordle.WORD_LENGTH:
            print(f"Word must be {wordle.WORD_LENGTH} characters long!")
            continue

        wordle.attempt(x)
        results = wordle.guess(x)
        print(*results, sep="\n")
        
    if Wordle.is_solved:
        print("You've guessed it right!!!")
    else:
        print("You failed to solve the puzzle!")

if __name__ == "__main__":
    main()