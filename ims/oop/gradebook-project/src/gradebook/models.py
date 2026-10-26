"""Domain objects for the gradebook."""

from .exceptions import InvalidScoreError


class Student:
    """A student and the scores recorded for them."""

    MIN_SCORE = 0
    MAX_SCORE = 100

    def __init__(self, student_id, name):
        if not student_id:
            raise ValueError("student_id must not be empty.")
        self.student_id = student_id
        self.name = name
        self._scores = []

    @property
    def scores(self):
        """Recorded scores as a read-only tuple."""
        return tuple(self._scores)

    def add_score(self, score):
        """Record a score after validating its range."""
        if not self.MIN_SCORE <= score <= self.MAX_SCORE:
            raise InvalidScoreError(score, self.MIN_SCORE, self.MAX_SCORE)
        self._scores.append(score)

    def average(self):
        """Mean of recorded scores, or 0.0 when there are none."""
        if not self._scores:
            return 0.0
        return sum(self._scores) / len(self._scores)

    def __repr__(self):
        return f"Student({self.student_id!r}, {self.name!r})"
