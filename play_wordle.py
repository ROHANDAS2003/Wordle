from typing import List
from letter_state import LetterState
from wordle import Wordle
from colorama import Fore

def main():
    print("Hello world!!!")
    wordle = Wordle("APPLE")

    while wordle.can_attempt:
        x = input("\nType our guess:  ")

        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f"Word must be {wordle.WORD_LENGTH} characters long!" + Fore.RESET)
            continue

        wordle.attempt(x)
        displa_results(wordle)
        
    if Wordle.is_solved:
        print("You've guessed it right!!!")
    else:
        print("You failed to solve the puzzle!")


def displa_results(wordle: Wordle):
    print("\nYour results so far:\n")
    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        print(colored_result_str)

    for _ in range(wordle.remining_attempts):
        print("_ " * wordle.WORD_LENGTH)
    
    print(f"\nYou have {wordle.remining_attempts} attempts remaining.\n")


def convert_result_to_color(result: List[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)
    return " ".join(result_with_color)

if __name__ == "__main__":
    main()