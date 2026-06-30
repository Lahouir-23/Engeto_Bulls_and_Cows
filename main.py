import random

def sec_num() -> str:
    first_digit = random.choice('123456789')
    remaining = list('0123456789')
    remaining.remove(first_digit)

    secret = first_digit + ''.join(random.sample(remaining, 3))
    return secret

secret = sec_num()

print('Hi There!')
print(47 * '_')
print('I have generated a random 4 digit number for you.')
print('Lets play a bulls and cows game.')
print(47 * '_')


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

    bulls = 0
    cows = 0

    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret and guess[i] != secret[i]:
            cows += 1

        if bulls == 1:
            bull_text = 'bull'
        else:
            bull_text = 'bulls'

        if cows == 1:
            cow_text = 'cow'
        else:
            cow_text = 'cows'

        print(f'{bulls} {bull_text} {cows} {cow_text}')

        if bulls == 4:
            print('YOU WIN')
            exit()
    if len(guess) != 4:
        print('Error, guess must be exactly 4 digits')

    if not guess.isdigit():
        print('Error, guess must be a number')

    elif guess[0] == '0':
       print('Guess can\'t start with 0')

    elif len(set(guess)) != 4:
        print('Error, guess can\'t contain dupplicate digits')

    bulls = 0
    cows = 0

    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret and guess[i] != secret[i]:
            cows += 1

        if bulls == 1:
            bull_text = 'bull'
        else:
            bull_text = 'bulls'

        if cows == 1:
            cow_text = 'cow'
        else:
            cow_text = 'cows'

        print(f'{bulls} {bull_text} {cows} {cow_text}')

        if bulls == 4:
            print('YOU WIN')
            exit()