import unittest
import string_stats

class TestMostCommonStrings(unittest.TestCase):
    def test_happy_path(self):
        """Test that it finds the rights strings"""
        letters = ["a", "b", "c", "d", "e", "f"]
        string_list = []
        for i in range(5): # adds the first 5 letters 5 times to the list
            string_list.extend([letters[l] for l in range(5)])
        # this f shouldn't show up in the results because there are only 1 of them
        string_list.append("f")
        # this e should show up first because there are the most of them
        string_list.append("d") 
        result = string_stats.most_common_strings(string_list)

        self.assertListEqual(result, [("d", 6), ("a",5), ("b", 5), ("c", 5), ("e",5)])

    def test_order_maintained_on_tie(self):
        """Test that it on ties for last out of the 5, the first items in the list win"""
        letters = ["a", "b", "c", "d", "e", "f"]
        string_list = []
        for i in range(6):
            string_list.extend([letters[l] for l in range(6)])
        result = string_stats.most_common_strings(string_list)

        self.assertListEqual(result, [("a", 6), ("b",6), ("c", 6), ("d", 6), ("e",6)])

    def test_fewer_than_5(self):
        """Test that when there are fewer than 5 different strings it still works"""
        letters = ["a", "b", "c"]
        string_list = []
        for i in range(3):
            string_list.extend([letters[l] for l in range(3)])
        string_list.append("d")
        result = string_stats.most_common_strings(string_list)

        self.assertListEqual(result, [("a", 3), ("b",3), ("c", 3), ("d", 1)])

class TestAverageStringLength(unittest.TestCase):
    def test_happy_path(self):
        """Test that it finds the rights strings"""
        letters = ["aaa", "bb", "cc", "dd", "ee", "f"]
        result = string_stats.average_length(letters)
        self.assertEqual(result, 2)

    def test_round_to_even(self):
        """Test that of the average is in between 2 numbers it rounds to the even number"""
        letters = ["aa", "bb", "ccc", "ddd"]
        result = string_stats.average_length(letters)
        self.assertEqual(result, 2)

class TestMostCommonFirstLetters(unittest.TestCase):
    def test_happy_path(self):
        """Test that if finds the right strings"""
        letters = ['ann', 'bnn', 'cnn', 'dnn', 'enn', 'fnn']
        string_list = []
        for i in range(0, 5):
            string_list.extend([letters[l] for l in range(0, 5)])
        string_list.append('fnn')
        string_list.append('dnn')
        result = string_stats.most_common_first_letters(string_list)
        self.assertListEqual(result, [('d', 6), ('a', 5), ('b', 5), ('c', 5), ('e', 5)])

    def test_order_maintained_on_tie(self):
        """Test that if on ties for last out of 5, the first items in the list win"""
        letters = ['ann', 'bnn', 'cnn', 'dnn', 'enn', 'fnn']
        string_list = []
        for i in range(0, 6):
            string_list.extend([letters[l] for l in range(0, 6)])
        result = string_stats.most_common_first_letters(string_list)
        self.assertListEqual(result, [('a', 6), ('b', 6), ('c', 6), ('d', 6), ('e', 6)])

    def test_fewer_than_5(self):
        """Test that it still works with a list fewer than 5 different starting letters"""
        letters = ['ann', 'bnn', 'cnn']
        string_list = []
        for i in range(6):
            string_list.extend([letters[l] for l in range(3)])
        result = string_stats.most_common_first_letters(string_list)
        self.assertListEqual(result, [('a', 6), ('b', 6), ('c', 6)])
        
class TestFindLetterLengthCorrelation(unittest.TestCase):
    def test_happy_path(self):
        """test that it finds the right strings"""
        letters = ['ann', 'bn', 'c', 'dnnn', 'ennnn', 'fnnnnn']
        result = string_stats.find_letter_length_correlation(letters)
        self.assertDictEqual(result, {'a': 3, 'b': 2, 'c': 1, 'd': 4, 'e': 5, 'f': 6})

    def test_round_to_even(self):
        """test that if the average is between to numbers it rounds to the even number"""
        letters = ['an', 'annnnnnnn', 'bnnn', 'bnnnn']
        result = string_stats.find_letter_length_correlation(letters)
        self.assertDictEqual(result, {'a': 6, 'b': 4})

if __name__ == '__main__':
    unittest.main()
