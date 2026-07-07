import random

def generate_sec_num() -> int:
    """
    Generuje 4 náhodná čísla s unikatními číslicemi.

    Vrací: tajné číslo
    """

    first_digit = random.choice('123456789')
    remaining = list('0123456789')
    remaining.remove(first_digit)

    secret = first_digit + ''.join(random.sample(remaining, 3))
    return int(secret)

def get_valid_guess() -> str:
    """
    Získa input uživatele a skontroluje zda je platný tip


     Vrací: platný tip uživatele
    """
    while True:
        guess = input('Please enter a number: ')

        if len(guess) != 4:
            print('Error, guess must be exactly 4 digits')

        if not guess.isdigit():
            print('Error, guess must be a number')

        elif guess[0] == '0':
           print('Guess can\'t start with 0')

        elif len(set(guess)) != 4:
            print('Error, guess can\'t contain dupplicate digits')

        return guess

def evaluate_guess(guess: str, secret: str) -> tuple[int, int]:
    """
    Porovná tip hráče s tajným číslem v def generate_sec_num a spočítá bulls a cows.

    Vrací: tuple (Bulls, cows)

    """
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret and guess[i] != secret[i]:
            cows += 1
    return bulls, cows

def print_score(bulls: int, cows: int) -> None:
        bull_text = 'bull' if bulls == 1 else 'bulls'
        cow_text = 'cow' if cows == 1 else 'cows'
        print(f'{bulls} {bull_text}, {cows} {cow_text}')

def main() -> None:
    """Hlavní funkce hry"""
    secret = generate_sec_num()
    secret = str(secret)

    print("Hi There!")
    print(47 * "_")
    print("I have generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print(47 * "_")

    while True:
        guess = get_valid_guess()
        bulls, cows = evaluate_guess(guess, secret)

        print_score(bulls, cows)

        if bulls == 4:
            print("YOU WIN!")
            break


if __name__ == "__main__":
    main()
