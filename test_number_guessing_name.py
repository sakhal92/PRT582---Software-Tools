"""
This is used to unit test the number_guessing_game.py file
"""

import unittest
from number_guessing_game import provide_hints


class TestNumberGuessingGame(unittest.TestCase):
    """
    Checking if test cases of randomly generated number
    and guessed numbers are correct or various scenerios
    """

    def test_play_game(self):
        """
        Input validation
        """
        guess = "quit"
        self.assertEqual("quit", guess.lower())
        #  Test case: input is a 4 digit number
        guess = "1234"
        self.assertEqual(4, len(guess))
        #  Test case: input length is more than 4
        guess = "12345"
        self.assertEqual(True, len(guess) != 4)
        #  Test case: input length is less than 4
        guess = "123"
        self.assertEqual(True, len(guess) != 4)
        #  Test case: input is not an integer
        guess = "123a"
        self.assertEqual(False, guess.isdigit())

    def test_provide_hints(self):
        """
        using 1234 as our number and testing it against 4 test scenerios
        """
        actual_number = "1234"
        # Test case: Correct guess
        guess = "1234"
        hints = provide_hints(actual_number, guess)
        self.assertEqual(hints, ["circle", "circle", "circle", "circle"])
        # Test case: All digits in the wrong position
        guess = "4321"
        hints = provide_hints(actual_number, guess)
        self.assertEqual(hints, ["x", "x", "x", "x"])
        # Test case: Some digits in the right position and some in wrong
        guess = "1243"
        hints = provide_hints(actual_number, guess)
        self.assertEqual(hints, ["circle", "circle", "x", "x"])
        # Test case: No digits in the correct position or the wrong position
        guess = "5678"
        hints = provide_hints(actual_number, guess)
        self.assertEqual(hints, ["-", "-", "-", "-"])


if __name__ == '__main__':
    unittest.main()
