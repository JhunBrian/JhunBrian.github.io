# ds212-gradebook

A small object-oriented gradebook used as the running example in the
DS212 lessons on packaging, testing, and distribution.

## Installation

```bash
pip install -e ".[dev]"
```

## Usage

```python
from gradebook import Gradebook, Student

book = Gradebook("DS212")
book.add(Student("2026-001", "Ana"))
book.record("2026-001", 92)
print(book.average("2026-001"))
```

## Running the tests

```bash
python -m pytest
```

## License

MIT
