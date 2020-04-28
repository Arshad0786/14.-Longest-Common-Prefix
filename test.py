import unittest
from LongestCommonPrefix import Solution


class TwoSumTest(unittest.TestCase):
    def test_basic_function(self):
        temp = Solution()
        self.input = ["trade","try","triangle"]
        self.assertEqual(temp.longestCommonPrefix(self.input), "tr")

    def test_no_common_prefix(self):
        temp = Solution()
        self.input = ["nice","well",'incredible']
        self.assertEqual(temp.longestCommonPrefix(self.input), "")

    def test_all_same_words(self):
        temp = Solution()
        self.input = ["test","test","test"]
        self.assertEqual(temp.longestCommonPrefix(self.input), "test")
    
    def test_empty_list(self):
        temp = Solution()
        self.input = []
        self.assertEqual(temp.longestCommonPrefix(self.input), "")

    def test_first_word_longer(self):
        temp = Solution()
        self.input = ["test","tes","te"]
        self.assertEqual(temp.longestCommonPrefix(self.input), "te")



if __name__ == "__main__":
    unittest.main()