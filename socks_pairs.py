from collections import Counter


def count_pairs(socks_list):
    return sum([num // 2 for num in Counter(socks_list).values()])


if __name__ == '__main__':
    input = [2, 4, 5, 4, 9, 7, 8, 9, 1, 9, 9, 9, 8, 4]
    print(Counter(input))
    print(count_pairs(input))
