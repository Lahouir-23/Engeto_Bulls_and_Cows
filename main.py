import random

NUM_DIGITS = 4
DIGITS = '0123456789'


def generate_sec_num() -> str:
    """
    Generuje tajné číslo s NUM_DIGITS unikátními číslicemi (první není 0).

    Vrací: tajné číslo jako řetězec
    """
    first_digit = random.choice(DIGITS[1:])
    remaining = list(DIGITS)
    remaining.remove(first_digit)

    secret = first_digit + ''.join(random.sample(remaining, NUM_DIGITS - 1))
    return secret


def get_valid_guess() -> str:
    """
    Získá input uživatele a zkontroluje, zda je platný tip.

    Vrací: platný tip uživatele
    """
    while True:
        guess = input(f'Please enter a {NUM_DIGITS}-digit number: ').strip()

        if len(guess) != NUM_DIGITS:
            print(f'Error, guess must be exactly {NUM_DIGITS} digits')
            continue

        if not guess.isdigit():
            print('Error, guess must contain only digits')
            continue

        if guess[0] == '0':
            print("Error, guess can't start with 0")
            continue

        if len(set(guess)) != NUM_DIGITS:
            print("Error, guess can't contain duplicate digits")
            continue

        return guess


def evaluate_guess(guess: str, secret: str) -> tuple[int, int]:
    """
    Porovná tip hráče s tajným číslem a spočítá bulls a cows.

    Vrací: tuple (bulls, cows)
    """
    bulls = 0
    cows = 0
    for guess_digit, secret_digit in zip(guess, secret):
        if guess_digit == secret_digit:
            bulls += 1
        elif guess_digit in secret:
            cows += 1
    return bulls, cows


def print_score(bulls: int, cows: int) -> None:
    bull_text = 'bull' if bulls == 1 else 'bulls'
    cow_text = 'cow' if cows == 1 else 'cows'
    print(f'{bulls} {bull_text}, {cows} {cow_text}')


def play_round() -> None:
    """Odehraje jedno kolo hry."""
    secret = generate_sec_num()

    print("Hi there!")
    print(47 * "_")
    print(f"I have generated a random {NUM_DIGITS}-digit number for you.")
    print("Let's play a bulls and cows game.")
    print(47 * "_")

    while True:
        guess = get_valid_guess()
        bulls, cows = evaluate_guess(guess, secret)

        print_score(bulls, cows)

        if bulls == NUM_DIGITS:
            print("YOU WON!")
            break


def main() -> None:
    """Hlavní funkce hry, umožňuje opakované hraní."""
    while True:
        play_round()

        again = input("Chceš hrát znovu? (ano/ne): ").strip().lower()
        if again not in ('ano', 'a', 'yes', 'y'):
            print("Díky za hru, ahoj!")
            break


if __name__ == "__main__":
    main()
