import unittest
# from clinic_files import Clinic


class TestClinic(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def dummyTest(self):
        print("Testing 1 2 3")
        self.assertTrue(True, "True")


# unittest.main()

print(__name__)
if __name__ == "__main__" or __name__ == "clinic_files.clinic_files_tester":
    print("Lets start")
    unittest.main()
