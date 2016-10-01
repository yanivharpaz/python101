import random


def input_number():
    input_ok = False
    while not input_ok:
        try:
            user_input = int(input('Try to guess my number ===> '))
            input_ok = True
        except ValueError:
            print('Please enter only decimal numbers.')
            continue

    return user_input


def check_guess(magic_number, guess_number):
    result_of_guess = False
    if guess_number > magic_number:
        print('Your guess is too high.')
    elif guess_number < magic_number:
        print('Your guess is too low.')
    else:
        result_of_guess = True
    return result_of_guess


def main():
    max_number = 10
    min_number = 1
    greeting_text = 'Greetings! I guessed a number between {0} and {1} . Want to try to guess it?'

    print(greeting_text.format(min_number, max_number))
    magic_number = random.randint(min_number, max_number)

    number_found = False

    while not number_found:
        user_guess = input_number()
        number_found = check_guess(magic_number,user_guess)

    guess_message = 'Number {0} was found correctly'
    print(guess_message.format(magic_number))


if __name__ == '__main__':
    main()
