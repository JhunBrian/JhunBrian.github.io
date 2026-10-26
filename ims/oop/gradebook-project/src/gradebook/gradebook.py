"""The Gradebook aggregate."""

from .exceptions import GradebookError, StudentNotFoundError


class Gradebook:
    """A collection of students for one course."""

    PASSING = 75

    def __init__(self, course_code):
        self.course_code = course_code
        self._students = {}

    def add(self, student):
        if student.student_id in self._students:
            raise GradebookError(f"{student.student_id} is already enrolled.")
        self._students[student.student_id] = student

    def get(self, student_id):
        try:
            return self._students[student_id]
        except KeyError:
            raise StudentNotFoundError(student_id) from None

    def record(self, student_id, score):
        self.get(student_id).add_score(score)

    def average(self, student_id):
        return self.get(student_id).average()

    def passing(self):
        """Students whose average meets the passing mark, best first."""
        result = [s for s in self._students.values() if s.average() >= self.PASSING]
        return sorted(result, key=lambda s: s.average(), reverse=True)

    def __len__(self):
        return len(self._students)

    def __contains__(self, student_id):
        return student_id in self._students
