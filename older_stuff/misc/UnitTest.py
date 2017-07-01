import os
import unittest

def analyze_text(filename):
    # with open(filename, 'r') as f:
    #     return sum(1 for _ in f)
    lines = 0
    chars =0
    with open(filename, 'r') as f:
        for line in f:
            lines +=1
            chars += len(line)
    return (lines,chars)

class TextAnalysisTests(unittest.TestCase):

    def setUp(self):
        self.filename =  'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('now we are engaged in a great civil war.\n'
                    'testing \n')

    def tearDown(self):
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        analyze_text(self.filename)

    def test_line_count(self):
        self.assertEqual(analyze_text(self.filename)[0], 2)

    def test_character_count(self):
        self.assertEqual(analyze_text(self.filename)[1], 90)

    def test_no_deletion(self):
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))


if __name__ == '__main__':
    unittest.main()
