# Course home

```{raw} html
<section class="course-hero" aria-label="Welcome to DS112">
  <div class="course-eyebrow">DS112 / The course companion</div>
  <p class="hero-title">Think in steps.<br>Compute with Python.</p>
  <p>Computer Programming for Data Science. Learn to plan algorithms, write clear Python, and analyze data with NumPy and pandas.</p>
  <div class="hero-actions">
    <a class="hero-button" href="notebooks/00_ProgrammingLanguages.html">Start learning <span aria-hidden="true">→</span></a>
    <a class="hero-button secondary" href="course-guide.html">How to use this book</a>
  </div>
</section>
<div class="course-meta">FIRST-YEAR DATA SCIENCE · USTP · COLLEGE OF INFORMATION TECHNOLOGY AND COMPUTING</div>
```

## Explore the course

Choose a module below, or follow the course navigation from top to bottom. **Seatworks** (practice) and graded **activities** appear beneath the lessons they support.

::::{grid} 1 1 2 2
:gutter: 3

:::{grid-item-card} 01 · Introduction to programming
:link: notebooks/00_ProgrammingLanguages
:link-type: doc

^^^
Programming languages and Python, algorithms and flowcharts, programming paradigms, and the Jupyter Notebook. *Weeks 2–3*

+++
Begin with programming languages →
:::

:::{grid-item-card} 02 · Python programming
:link: notebooks/04_VariablesExpressions
:link-type: doc

^^^
Variables and expressions, control structures, functions, lists, tuples, strings, dictionaries, files, exceptions, and a first look at classes. *Weeks 4–8*

+++
Start writing Python →
:::

:::{grid-item-card} 03 · NumPy
:link: notebooks/11_IntroNumPy
:link-type: doc

^^^
Fast numerical arrays: 1D and 2D operations, broadcasting, universal functions, axes, and reshaping. *Weeks 10–12*

+++
Start NumPy →
:::

:::{grid-item-card} 04 · pandas
:link: notebooks/15_IntroPandas
:link-type: doc

^^^
Series and DataFrames, reading data, selection, visualization, grouping, merging, and pivot tables. *Weeks 13–16*

+++
Start pandas →
:::

:::{grid-item-card} 05 · Integrated PyData project
:link: notebooks/23_PyDataProject
:link-type: doc

^^^
Bring everything together in a tested, reproducible data analysis project and presentation. *Weeks 13–17*

+++
Read the project guide →
:::

:::{grid-item-card} Paradigms throughout the course
:link: notebooks/02_ProgrammingParadigms
:link-type: doc

^^^
Structured, procedural, and functional thinking — introduced in Week 3, revisited with real data in Week 16.

+++
Explore programming paradigms →
:::
::::

[View the course syllabus](syllabus.md) · [How to use this book](course-guide.md) · [Datasets](datasets.md) · [Midterm review guide](notebooks/MidtermReview.ipynb)

## Welcome

Welcome to **Computer Programming for Data Science**, the first programming course of the BS Data Science program. No prior programming experience is assumed.

Data scientists spend much of their time **writing programs**: programs that collect data, clean it, compute with it, and present what it means. In this course, you will learn to think like a programmer — to break a problem into **precise steps** — and to express those steps in **Python**, the most widely used language in data science.

```text
Problem → Algorithm → Python program → Data analysis with NumPy & pandas → Insight
```

## How this course is organized

The course follows a path from **thinking** to **coding** to **analyzing**:

1. **Introduction to programming.** What programs and programming languages are, how to design **algorithms** and draw **flowcharts**, the main **programming paradigms**, and how to work in **Jupyter notebooks**.
2. **Python programming.** The core language: variables, control structures, functions, data structures, files, exceptions, and objects.
3. **NumPy.** Fast computation with arrays — the foundation of scientific Python.
4. **pandas.** Working with real tables of data: selecting, cleaning, grouping, merging, reshaping, and visualizing.
5. **Integrated project.** A complete, reproducible data analysis presented to the class.

## A note on paradigms

This course places special emphasis on three ways of organizing programs:

* **Structured programming** — building every program from sequence, selection, and iteration;
* **Procedural programming** — decomposing problems into well-named, reusable functions;
* **Functional programming** — transforming data through pure functions and pipelines, the style behind NumPy and pandas.

Look for the **Paradigm lens** notes throughout the book. They show which way of thinking each new tool belongs to.

```{admonition} A note to learners
:class: tip

Programming is learned by doing. Read each example, **predict** what it will print, run it, and then change it to see what happens. Mistakes and error messages are a normal part of learning — read them carefully; they tell you what went wrong.
```

## About this material

This Jupyter Book is an instructional resource of the **Department of Data Science, USTP**, for **DS112 — Computer Programming**. It follows the official course syllabus and draws on the course's instructional materials and the readings listed in the syllabus. Every page ends with its references.
