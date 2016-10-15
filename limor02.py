import sys


def main(argv):
    print("This is my program")
    if len(argv) > 1:
        print("first argument is ", argv[1])


if __name__ == '__main__':
    main(sys.argv)
