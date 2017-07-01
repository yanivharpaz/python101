from pprint import pprint as pp
import sys


def main():
    print(sys.argv)
    if len(sys.argv) !=3:
        sys.exit('usage:{} [src] [dest]'.format(sys.argv[0]))

    _, src, dest = sys.argv
    with open(src, 'rb') as infile, open(dest, 'wb') as outfile:
        while True:
            data = infile.read(1024)
            if not data:
                break
            outfile.write(data)

if __name__ == '__main__':
    main()






pp(x_x)