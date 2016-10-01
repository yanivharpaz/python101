import random



def get_random_word():
    words = ['pizza', 'cheese', 'apples']

    return words[random.randint(0,3)]

def play_game():
    print('Playing game')
    word = get_random_word()
    strikes = 0
    max_strikes = 3

    playing = True

    while playing:
        strikes += 1

        if strikes >= max_strikes:
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

