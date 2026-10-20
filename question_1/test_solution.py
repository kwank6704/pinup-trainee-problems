import unittest

from solution import run


class LogicChallengeTest(unittest.TestCase):
    def test_final_answers(self):
        answer, _ = run()
        self.assertEqual(answer["A"], 82)
        self.assertEqual(answer["B"], 374)

    def test_final_box_values(self):
        _, box = run()
        self.assertEqual(box[1], 860)  # never touched by the program
        self.assertEqual(box[2], 105)
        self.assertEqual(box[3], 374)
        self.assertEqual(box[4], 479)
        self.assertEqual(box[5], 48)


if __name__ == "__main__":
    unittest.main()
