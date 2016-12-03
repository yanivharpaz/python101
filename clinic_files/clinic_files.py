from __future__ import print_function
import sys
import _mssql


class Files(object):
    def __init__(self):
        self.files = dict()

    def load(self):
        pass


class Clinic(object):
    def __init__(self):
        self.clinic_list = dict()

    def load(self):
        pass


def main(argv):
    files = Files()
    clinic = Clinic()
    print("Hello XML")


if __name__ == "__main__":
    main(sys.argv)
