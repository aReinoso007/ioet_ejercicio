import unittest
from worker_functions import WorkerFunctions as worker


class TestReadFile(unittest.TestCase):

    def test_init(self):
        self.assertEqual(
            worker("sample.txt").file, "sample.txt"
        )

    def test_read_file(self):
        fileInput = []
        fileInput = worker("sample.txt").readFile()
        for f in fileInput:
            containsEqual = sum(1 for fileInput in f if '=' in fileInput)
            containsSpaces = sum(1 for fileInput in f if ' ' in fileInput)

        if(containsEqual > 0 | containsSpaces > 0):
            self.assertFalse
        else:
            self.assertTrue

    def test_run_process(self):
        result = worker("sample.txt").runProcess()
        expectedResult1 = {"'RENE'-'ASTRID'": 2,
                           "'RENE'-'ANDRES'": 2,
                           "'ASTRID'-'ANDRES'": 3}

        expectedResult2 = {"'RENE'-'ASTRID'": 3}

        if (result == expectedResult1) | (result == expectedResult2):
            self.assertTrue
        else:
            self.assertFalse


if __name__ == "__main__":
    unittest.main()
