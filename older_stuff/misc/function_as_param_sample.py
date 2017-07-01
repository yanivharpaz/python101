def get_words():
    '''
    Produce words
    '''
    visible_texts = ['hello', 'there', 'how', 'are', 'you', 'doing', 'my', 'friend']
    return visible_texts


def produce_names_and_numbers():
    '''
    Produce numbers
    '''
    my_numbers = [my_num for my_num in range(30)]
    return my_numbers


def launch_printers(words, nums, print_func):
    '''
    generic print
    '''
    for word, num in zip(words, nums):
        print_func(word, num)


def print_plus(word, num):
    print('+' * (len(word) + len(str(num)) + 7))
    print('+', word, '+', num, '+')
    print('+' * (len(word) + len(str(num)) + 7))


def print_minus(word, num):
    print('-' * (len(word) + len(str(num)) + 7))
    print('-', word, '-', num, '-')
    print('-' * (len(word) + len(str(num)) + 7))


'''
main
'''
if __name__ == '__main__':
    '''
    init data
    '''
    nums = produce_names_and_numbers()
    words = get_words()

    '''
    launch the print
    '''
    launch_printers(words, nums, print_plus)
    launch_printers(words, nums, print_minus)

