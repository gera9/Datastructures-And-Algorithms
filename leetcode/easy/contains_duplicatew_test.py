import unittest
from contains_duplicate import contains_duplicate


class TestContainsDuplicate(unittest.TestCase):
    test_cases = [
        {
            "name": "contains_duplicate_true",
            "nums": [1, 2, 3, 1],
            "expected": True
        },
        {
            "name": "contains_duplicate_false",
            "nums": [1, 2, 3, 4],
            "expected": False
        },
        {
            "name": "contains_duplicate_empty",
            "nums": [],
            "expected": False
        },
        {
            "name": "contains_duplicate_single",
            "nums": [1],
            "expected": False
        },
        {
            "name": "contains_duplicate_two",
            "nums": [1, 1],
            "expected": True
        },
        {
            "name": "contains_duplicate_two_false",
            "nums": [1, 2],
            "expected": False
        }
    ]

    def test_contains_duplicate(self):
        for test_case in self.test_cases:
            with self.subTest(test_case["name"]):
                self.assertEqual(contains_duplicate(
                    test_case["nums"]), test_case["expected"])


if __name__ == "__main__":
    unittest.main()
