import random



def get_random_word():
    words = ['pizza', 'cheese', 'apples']

    return words[random.randint(0,len(words) - 1)]

def display_word(word):
    for letter_counter in word:
        print(letter_counter, ' ', end='')

    print('')


def get_guess():
    guessed_char = input('Please enter a character you guess is in the word ==> ')
    return guessed_char


def check_word(letter, secret_word, blanked_word):
    found = False
    for letter_iterator in range(0, len(secret_word)):
        if letter == secret_word[letter_iterator]:
            found = True
            blanked_word[letter_iterator] = letter
    return found


def play_game():
    print('Playing game')
    word = get_random_word()
    strikes = 0
    max_strikes = 3

    blanked_word = list('_' * len(word))

    playing = True

    while playing:
        display_word(blanked_word)
        letter = get_guess()

        if not check_word(letter, word, blanked_word):
            strikes += 1

        if strikes >= max_strikes:
            playing = False

        if not '_' in blanked_word:
            display_word(blanked_word)
            playing = False

    if strikes >= max_strikes:
        print("Sorry, you lost.")
    else:
        print("Winner, you guessed right.")


def main():
    print('Word game started.')
    play_game()

    print('Game has ended, thank you for participating.')


if __name__ == '__main__':
    main()

