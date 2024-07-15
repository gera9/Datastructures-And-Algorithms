import unittest
from anagrams import is_anagram


class TestIsAnagram(unittest.TestCase):
    test_cases = [
        {
            "name": "anagram_true",
            "s": "anagram",
            "t": "nagaram",
            "expected": True
        },
        {
            "name": "anagram_false",
            "s": "hello",
            "t": "world",
            "expected": False
        },
        {
            "name": "anagram_empty",
            "s": "",
            "t": "",
            "expected": True
        },
        {
            "name": "anagram_single",
            "s": "a",
            "t": "a",
            "expected": True
        },
        {
            "name": "anagram_different_length",
            "s": "hello",
            "t": "worlds",
            "expected": False
        },
        {
            "name": "anagram_single_false",
            "s": "a",
            "t": "b",
            "expected": False
        }
    ]

    def test_is_anagram(self):
        for test_case in self.test_cases:
            with self.subTest(test_case["name"]):
                self.assertEqual(is_anagram(
                    test_case["s"], test_case["t"]), test_case["expected"])


if __name__ == "__main__":
    unittest.main()
