import unittest

from src.controllers import FindAccessCodeWithKeyLogsController


class FindAccessCodeWithKeyLogsTestCase(unittest.TestCase):
    def test_find_access_code_(self):
        keylogs = [
            [3, 1, 9], [6, 8, 0], [1, 8, 0], [6, 9, 0], [1, 2, 9], [6, 2, 0], [7, 6, 2], [6, 8, 9], [7, 6, 2],
            [3, 1, 8], [3, 6, 8], [7, 1, 0], [7, 2, 0], [7, 1, 0], [6, 2, 9], [1, 6, 8], [1, 6, 0], [6, 8, 9],
            [7, 1, 6], [7, 3, 1], [7, 3, 6], [7, 2, 9], [3, 1, 6], [7, 2, 9], [7, 2, 9], [7, 1, 0], [7, 6, 9],
            [2, 9, 0], [7, 1, 9], [6, 8, 0], [3, 1, 8], [3, 8, 9], [1, 6, 2], [2, 8, 9], [1, 6, 2], [7, 1, 8],
            [7, 2, 9], [3, 1, 9], [7, 9, 0], [6, 8, 0], [8, 9, 0], [3, 6, 2], [3, 1, 9], [7, 6, 0], [3, 1, 6],
            [7, 2, 9], [3, 8, 0], [3, 1, 9], [7, 2, 8], [7, 1, 6]
        ]

        access_code = FindAccessCodeWithKeyLogsController.find_access_code_in_keylogs(keylogs)

        self.assertEqual(access_code, '73162890')


if __name__ == '__main__':
    unittest.main()
