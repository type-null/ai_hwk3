
import unittest
import hwk3_tr

class TestMyModule(unittest.TestCase):

    def setUp(self): # run before test runs
        return # do nothing

    def test_clean_text(self):
        tweet = "RT @dullalena @taurusismagic @motshabi_P ❤❤ \
        I'm happy you had a beautiful day! 😘 https://t.co/T6uxfX6DpC"
        
        result = hwk3_tr.clean_text(tweet)
        expected_result = "❤❤ I'm happy you had a beautiful day! 😘"
        self.assertEqual(result, expected_result)

    def test_tokenize_text(self):
        cleaned_text = "I'm happy you had a beautiful day!"

        result = hwk3_tr.tokenize_text(cleaned_text)
        expected_result = ["I'm", "happy", "beautiful", "day", "!"]
        self.assertEqual(result, expected_result)

    def test_replace_token_with_index(self):
        return

    def test_pad_sequence(self):
        return

    def test_one_for_all(self):
        return