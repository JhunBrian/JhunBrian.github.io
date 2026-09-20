# Course home

```{raw} html
<section class="course-hero" aria-label="Welcome to DS212">
  <div class="course-eyebrow">DS212 / The course companion</div>
  <p class="hero-title">Think in objects.<br>Build with Python.</p>
  <p>Object-Oriented Programming for Data Science. Explore the ideas, work through the examples, and turn your understanding into practice.</p>
  <div class="hero-actions">
    <a class="hero-button" href="notebooks/00_Introduction.html">Start learning <span aria-hidden="true">→</span></a>
    <a class="hero-button secondary" href="course-guide.html">How to use this book</a>
  </div>
</section>
<div class="course-meta">SECOND-YEAR DATA SCIENCE · USTP · COLLEGE OF INFORMATION TECHNOLOGY AND COMPUTING</div>
```

## Explore the course

Choose a lesson below, or follow the course navigation from top to bottom. Practice activities appear beneath the lessons they support.

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} OOP foundations
:link: notebooks/00_Introduction
:link-type: doc

^^^
Explore programming paradigms and the history of object-oriented thinking. Put the ideas to work in two guided activities.

+++
Begin with programming paradigms →
:::

:::{grid-item-card} Python review
:link: notebooks/02_PythonReview1
:link-type: doc

^^^
Revisit Python fundamentals, then move through control flow, functions, and modules before the combined coding exercise.

+++
Start Python review I →
:::
::::

[View the course syllabus](syllabus.md) · [Go to the Python coding exercise](notebooks/exercises/02_Exercise.ipynb)

## Welcome

Welcome to **Object-Oriented Programming for Data Science**, an instructional resource designed to introduce Data Science students to the principles, techniques, and practical applications of **Object-Oriented Programming (OOP) using Python**.

At this stage, you are already expected to be familiar with Python programming fundamentals such as variables, data types, conditional statements, loops, functions, collections, and basic problem solving. This material builds upon that foundation and introduces a different way of thinking about programs: not simply as sequences of instructions, but as systems composed of **objects that contain data and behavior**.

Object-Oriented Programming provides a way of organizing increasingly complex programs into understandable and reusable components. Rather than placing all functionality into a single program or collection of unrelated functions, OOP allows us to model concepts as objects and define how those objects interact.

Consider a simple Data Science workflow:

```text
Dataset → Preprocessing → Model → Evaluation → Results
```

Each component has its own data, responsibilities, and operations. Object-oriented design allows us to represent these components as cooperating objects rather than treating the entire workflow as one large program.

---

## Why OOP for Data Science?

Data Science is often introduced through individual scripts and notebooks. A typical program may load a dataset, clean the data, perform analysis, train a model, and generate visualizations.

This works well for smaller problems. As projects become larger, however, code can become difficult to organize, reuse, test, and maintain.

Object-Oriented Programming provides techniques for managing this complexity.

Through OOP, we can represent Data Science concepts using classes and objects. A dataset can become an object responsible for managing data. A preprocessing component can encapsulate transformation procedures. A machine learning model can provide methods for training and prediction. An experiment can contain its configuration, model, results, and evaluation metrics.

For example:

```python
dataset = Dataset("students.csv")

dataset.load()
dataset.clean()

model = ClassificationModel()
model.fit(dataset)

results = model.evaluate(dataset)
```

The goal is not simply to make programs longer or more sophisticated. The goal is to make programs **organized, understandable, reusable, and easier to extend**.

---

## Object-Oriented Thinking

Learning OOP involves more than learning Python syntax.

Writing:

```python
class Student:
    pass
```

is easy.

Determining **what should become a class, what information an object should contain, what operations it should perform, and how different objects should interact** requires a deeper understanding of software design.

Throughout this material, you will learn to think about programs in terms of:

* **Objects** — individual entities that contain state and behavior;
* **Classes** — definitions used to describe and create objects;
* **Attributes** — information maintained by an object;
* **Methods** — operations that an object can perform;
* **Encapsulation** — organizing and controlling access to an object's internal state;
* **Inheritance** — creating related classes that share or extend behavior;
* **Polymorphism** — allowing different objects to respond to common operations in their own ways;
* **Abstraction** — representing essential characteristics while managing unnecessary implementation details; and
* **Relationships between objects** — designing programs as systems of cooperating components.

These concepts will be explored through Python implementations, diagrams, examples, and programming exercises.

---

## Connecting OOP to the Data Science Ecosystem

Object-Oriented Programming is particularly relevant to Data Science because many of the Python libraries commonly used in the field are designed around objects.

When working with **NumPy**, **pandas**, **Matplotlib**, **scikit-learn**, and other Data Science libraries, you are already interacting with classes and objects.

For example:

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["Ana", "Ben", "Carlo"],
    "Score": [89, 92, 85]
})
```

`df` is not simply a table. It is an object created from the `DataFrame` class. It contains data and provides operations through methods such as:

```python
df.head()
df.describe()
df.dropna()
df.sort_values("Score")
```

The same idea appears in machine learning:

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

Here, `model` is an object. It maintains information about a trained model and provides behaviors such as `fit()` and `predict()`.

Understanding OOP therefore helps us understand not only **how to create our own software**, but also **how many of the tools used throughout the Python Data Science ecosystem are designed**.

---

## From Python Programmer to Software Designer

A major objective of this material is to move beyond knowing *how to make Python execute a task*.

As programs become larger, another question becomes increasingly important:

> **How should the program be designed?**

Two programs may produce exactly the same output while having very different designs. One may be difficult to modify and reuse, while another may be organized into components that can easily be extended to solve related problems.

Throughout this course, you will encounter problems that require you to make these design decisions.

You will create classes, instantiate and manipulate objects, represent relationships using class diagrams, reuse behavior through inheritance, redefine behavior through method overriding, and gradually apply these ideas to problems related to Data Science.

The emphasis is therefore not only on writing code that **works**, but on writing code whose structure has a clear purpose.

---

## Learning Through Practice

Object-Oriented Programming is best understood by designing and implementing programs.

This instructional material therefore combines conceptual discussions with Python examples, visual representations, and programming exercises. You are encouraged to modify examples, experiment with implementations, observe program behavior, and develop alternative solutions.

Some problems may have several valid designs.

When this happens, consider questions such as:

**What objects exist in the problem?**

**What responsibilities should each object have?**

**What data should an object maintain?**

**Which operations belong to which class?**

**How should the classes relate to one another?**

**Can parts of the program be reused?**

**Would this design remain understandable if the program became larger?**

These questions are fundamental to object-oriented software development.

---

## Learning Goal

By the end of this material, students should be able to **understand, design, and implement object-oriented Python programs and recognize how object-oriented principles are applied within the Data Science ecosystem**.

More importantly, students should be able to approach a programming problem not only by asking:

> *"What code should I write?"*

but also:

> *"How should I organize this program?"*

This shift in perspective is one of the central ideas of Object-Oriented Programming and an important step toward developing larger, reusable, and maintainable Data Science applications.

---

```{admonition} A Note to Learners
:class: tip

Do not treat Object-Oriented Programming as a collection of Python keywords that need to be memorized. Focus on understanding **why classes are designed in a particular way and how objects work together to solve a problem**.

Experiment with the examples, modify the code, make mistakes, and examine what happens. Programming is learned through practice.
```

---

## About This Material

This Jupyter Book is developed as an **open instructional resource for Object-Oriented Programming in Data Science**. It is intended primarily for undergraduate Data Science students who already possess foundational knowledge of Python programming.

The material may also be used by other learners and educators interested in studying Object-Oriented Programming through Python, particularly within a Data Science context.

Examples, discussions, diagrams, and exercises are provided to support both classroom instruction and independent study.