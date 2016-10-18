import sys

from math import log


def main(argv):
    print("This is my program")
    if len(argv) > 1:
        print("first argument is ", argv[1])


if __name__ == '__main__':
    main(sys.argv)


def convert(s):
    try:
        x=int(s)
        print("convert success!", x)
    except (ValueError,TypeError):
        x = -1
        print("convert failed!", x)
    return x

#convert(5)
#convert([1,2,3])
#convert("limor")


def convert_error(a):
    try:
        return int(a)
    except (ValueError,TypeError) as e:
        print("convertion error:{}".format(str(e)),file=sys.stderr)
        return -1

convert_error("lim")


def string_log(s):
    v = convert(s)
    return log(v)

string_log("1")