"""Exceptions raised by the gradebook package."""


class GradebookError(Exception):
    """Base class for all gradebook errors."""


class InvalidScoreError(GradebookError):
    """Raised when a score is outside the allowed range."""

    def __init__(self, score, low=0, high=100):
        self.score = score
        super().__init__(f"Score {score} is outside the range {low}-{high}.")


class StudentNotFoundError(GradebookError):
    """Raised when a student ID is not in the gradebook."""

    def __init__(self, student_id):
        self.student_id = student_id
        super().__init__(f"No student with ID {student_id!r}.")
