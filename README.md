# Physics Textbook Solutions in LaTeX

This is a collection of solutions to exercises and problems from various physics textbooks typeset
in LaTeX. The solutions are written by me, and are not guaranteed to be correct.

---

## Textbooks

- John R. Taylor [*Classical Mechanics*](/taylor)
- David J. Griffiths [*Introduction to Electrodynamics*](/griffiths_em)

Each Textbook has its own directory which contains the LaTeX source files and compiled pdfs of the
solutions. The source files are written in a modular fashion using the `subfiles` package, with each
chapter having its own file.

---

### Directory Structure

```
textbook/
├── main.tex
├── main.pdf
├── custom.sty
├── chapters/
│   ├── chapter1.tex
│   ├── chapter1.pdf
│   ├── chapter2.tex
│   └── chapter2.pdf
├── code/
│   ├── chapter1.ipynb
│   └── chapter2.py
└── images/
    └── figure.png
```

- `main.tex` is the main file which contains the preamble and imports the chapters.
- `main.pdf` is the compiled pdf of the solutions.
- `custom.sty` is a custom style file which contains custom commands and packages.
- `chapters/` is a directory containing the chapter files.
- `code/` is a directory containing the code files.
- `images/` is a directory containing the image files.

