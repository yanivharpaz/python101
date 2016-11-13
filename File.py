# f = open('wasteland.txt', mode='wt', encoding='utf-8')
# f.write('hi test')
# f.closed()
#
# g = open('wasteland.txt', mode='rt', encoding='utf-8')
# g.read()
#
# g.seek(0)
#
# g.readline()
#
# g.readlines()
#
# g.close()
#
# h = open('wasteland.txt', mode='at', encoding='utf-8')
# h.writelines(['limor study ,\n', 'python\n'])
#
# h.closed()

import sys

def main(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f:
        sys.stdout.write(line)
    f.close()

if __name__== '__main__':
    #main(sys.argv[1])
     main('wasteland.txt')