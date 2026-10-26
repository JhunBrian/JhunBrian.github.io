import unittest

from gradebook import InvalidScoreError, Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("2026-001", "Ana")

    def test_average_of_recorded_scores(self):
        for score in (90, 80, 85):
            self.student.add_score(score)
        self.assertAlmostEqual(self.student.average(), 85.0)

    def test_average_without_scores_is_zero(self):
        self.assertEqual(self.student.average(), 0.0)

    def test_rejects_score_above_range(self):
        with self.assertRaises(InvalidScoreError):
            self.student.add_score(101)

    def test_scores_are_read_only(self):
        self.student.add_score(90)
        self.assertIsInstance(self.student.scores, tuple)

    def test_empty_id_is_rejected(self):
        with self.assertRaises(ValueError):
            Student("", "Nobody")


if __name__ == "__main__":
    unittest.main()
