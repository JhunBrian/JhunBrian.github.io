import unittest

from gradebook import Gradebook, GradebookError, Student, StudentNotFoundError


class TestGradebook(unittest.TestCase):
    def setUp(self):
        self.book = Gradebook("DS212")
        self.book.add(Student("001", "Ana"))
        self.book.add(Student("002", "Ben"))

    def test_record_and_average(self):
        self.book.record("001", 90)
        self.book.record("001", 70)
        self.assertEqual(self.book.average("001"), 80)

    def test_unknown_student(self):
        with self.assertRaises(StudentNotFoundError):
            self.book.record("999", 90)

    def test_duplicate_student(self):
        with self.assertRaises(GradebookError):
            self.book.add(Student("001", "Another Ana"))

    def test_passing_sorted_best_first(self):
        self.book.record("001", 80)
        self.book.record("002", 95)
        names = [s.name for s in self.book.passing()]
        self.assertEqual(names, ["Ben", "Ana"])

    def test_len_and_contains(self):
        self.assertEqual(len(self.book), 2)
        self.assertIn("002", self.book)


if __name__ == "__main__":
    unittest.main()
