
# AI Engineering Tutorial

> A comprehensive lecture series covering the full stack of AI engineering—from Python fundamentals to production systems.

**Instructor:** Ali Pilehvar Meibody  
**Organization:** [Fanavari Co.](https://fanavari.co)  
**License:** MIT

<p align="center">
  <img src="Pictures/apm_pic.png" alt="AI Engineering" width="400"/>
</p>

---

## Overview

This repository contains lecture materials and implementations for a professional AI Engineering course. The curriculum extends beyond traditional machine learning to encompass the entire engineering foundation: numerical computing, data science, visualization, ML/DL pipelines, AI agents, databases, and DevOps tooling (Linux, CLI, Git).

---

## Curriculum Structure

| Module | Topic | Description | File |
|--------|-------|-------------|------|
| **01** | Python Review | Variables, types, control flow, functions, classes, iterables | [AI_Python_Review.py](AI_Tutorials/AI_Python_Review.py) |
| **02** | Advanced OOP | Object-oriented design, `@property`, `@staticmethod`, `@classmethod`, encapsulation | [ADVANCED_Class_Object.py](AI_Tutorials/ADVANCED_Class_Object.py) |
| **03** | CLI & Shell | Bash, navigation, file management, text editors (vim/nano), networking tools | [AI_CLI.md](AI_Tutorials/AI_CLI.md) |
| **04** | Git & Version Control | Local versioning, staging, commits, GitHub, project supervision | [AI_GIT.md](AI_Tutorials/AI_GIT.md) |
| **05** | Telegram Bots | Bot setup, handlers (command, message, callback), inline keyboards, conversation flow | [telegram_tutorial/](telegram_tutorial/README.md) |
| **06** | NumPy | Arrays, indexing, slicing, broadcasting, linear algebra, numerical computation | [AI_NUMPY.py](AI_Tutorials/AI_NUMPY.py) |
| **07** | Matplotlib | Visualization and graphics with matplotlib | [AI_Matplotlib.ipynb](AI_Tutorials/AI_Matplotlib.ipynb) |
| **08** | Linear Algebra | Vectors, matrices, transformations, eigenvalues, and core algebra for AI | [AI_Linear_Algebra.py](AI_Tutorials/AI_Linear_Algebra.py) |
| **09** | Calculus | Derivatives, gradients, optimization intuition, and calculus essentials for ML | [AI_Calculus.py](AI_Tutorials/AI_Calculus.py) |
| **10** | Numerical Methods | Numerical stability, approximation, and computational techniques | [AI_Numerical.py](AI_Tutorials/AI_Numerical.py) |
---

## Reviews

| Review | Topic | File |
|--------|-------|------|
| **R01** | Python Review | [AI_Python_Review.py](AI_Tutorials/AI_Python_Review.py) |
| **R02** | 24 bahman | [Reviews/01_24bahman.py](Reviews/01_24bahman.py) |
| **R03** | 7 esfand | [Reviews/02_7Esfand_1404.md](Reviews/02_7Esfand_1404.md)|

## Quiz

Tamame tamrin ha dakhele `Quiz/` folder hastand k bayad dar **repo** e k sakhtid ersal beshan

| Quiz | Focus | Suggested Prerequisite | File |
|------|-------|------------------------|------|
| **Q1** | Advanced Python, class methods, and errors | Modules 01-02 | [Q1.md](Quiz/Q1.md) |
| **Q2** | CLI and Git workflow practice | Modules 03-04 | [Q2.md](Quiz/Q2.md) |
| **Q3** | NumPy exercises | Module 06 | [Q3.md](Quiz/Q3.md) |
| **Q4** | Matplotlib exercises | Module 07 | [Q4.md](Quiz/Q4.md) |


---

## Repository Structure

```
AIEngineeringToturial/
├── README.md
├── LICENSE
│
├── pictures/
│   └── apm_pic.png
│
├── telegram_tutorial/        # 05: Telegram bots (python-telegram-bot)
│   ├── README.md
│   ├── telegram_server.py
│   └── telegram_test1.py … telegram_test7.py
│
├── AI_Tutorials/
│   ├── README.md                  # Study guide and reading sequence
│   ├── AI_Python_Review.py       # 01: Python fundamentals review
│   ├── ADVANCED_Class_Object.py  # 02: Advanced classes and OOP
│   ├── AI_CLI.md                 # 03: Command Line Interface & Shell
│   ├── AI_GIT.md                 # 04: Git, GitHub, version control
│   ├── AI_NUMPY.py               # 06: NumPy
│   ├── AI_Matplotlib.ipynb       # 07: Matplotlib
│   ├── AI_LINUX.md               # Linux & DevOps
│   ├── AI_Linear_Algebra.py
│   ├── AI_Calculus.py
│   └── AI_Numerical.py
│
├── Reviews/                  # Review / summary files
│   ├── 01_24bahman.py
│   ├── 02_7Esfand_1404.md
│
└── Quiz/                     # Practice assignments
    ├── README.md
    ├── Q1.md
    ├── Q2.md
    ├── Q3.md
    └── Q4.md

```

---

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/APMaii/AIEngineeringToturial.git
   cd AIEngineeringToturial
   ```

2. **Set up environment** (recommended: Conda or venv)
   ```bash
   conda create -n ai_eng python=3.10
   conda activate ai_eng
   pip install numpy pandas matplotlib scikit-learn
   ```

3. **Follow the modules** in order: Python Review → Advanced OOP → CLI → Git → NumPy → Pandas → Matplotlib → ML → DL → Agents & Databases → Linux.

---

## Learning Path

```
Python Review → Advanced OOP → CLI → Git
        ↓
NumPy → Pandas → Matplotlib
        ↓
Machine Learning → Deep Learning
        ↓
Agents & Databases → Linux & DevOps
```

---

## Collaboration

For questions, exercises, or collaboration:

- **Email1:** [alipilehvar1999@gmail.com](alipilehvar1999@gmail.com)
- **Email2:** [ali.pilehvarmeibody@studenti.polito.it](ali.pilehvarmeibody@studenti.polito.it)
- **Email3:** [ali.pilehvarmeibody@epfl.ch](ali.pilehvarmeibody@epfl.ch)

- **Repository:** Open issues or pull requests for contributions.

---

## References

- [Python Built-in Functions](https://docs.python.org/3/library/functions.html)
- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Git Documentation](https://git-scm.com/doc)

---

*© 2026 Ali Pilehvar Meibody · Fanavari Co. · MIT License*
