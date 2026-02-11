
# AI Engineering Tutorial

> A comprehensive lecture series covering the full stack of AI engineering—from Python fundamentals to production systems.

**Instructor:** Ali Pilehvar Meibody  
**Organization:** [Fanavari Co.](https://fanavari.co)  
**License:** MIT

<p align="center">
  <img src="apm_pic.png" alt="AI Engineering" width="400"/>
</p>

---

## Overview

This repository contains lecture materials and implementations for a professional AI Engineering course. The curriculum extends beyond traditional machine learning to encompass the entire engineering foundation: numerical computing, data science, visualization, ML/DL pipelines, AI agents, databases, and DevOps tooling (Linux, CLI, Git).

---

## Curriculum Structure

| Module | Topic | Description | File |
|--------|-------|-------------|------|
| **01** | Python Review | Variables, types, control flow, functions, classes, iterables | [AI_Python_Review.py](AI_Python_Review.py) |
| **02** | Advanced OOP | Object-oriented design, `@property`, `@staticmethod`, `@classmethod`, encapsulation | [ADVANCED_Class_Object.py](ADVANCED_Class_Object.py) |
| **03** | CLI & Shell | Bash, navigation, file management, text editors (vim/nano), networking tools | [AI_CLI.md](AI_CLI.md) |
| **04** | Git & Version Control | Local versioning, staging, commits, GitHub, project supervision | [AI_GIT.md](AI_GIT.md) |
| **05** | Telegram Bots | Bot setup, handlers (command, message, callback), inline keyboards, conversation flow | [telegram_tutorial/](telegram_tutorial/README.md) |

---

## Repository Structure

```
AIEngineeringToturial/
├── README.md
├── LICENSE
│
├── AI_Python_Review.py       # 01: Python fundamentals review
├── ADVANCED_Class_Object.py  # 02: Advanced classes and OOP
├── AI_CLI.md                 # 03: Command Line Interface & Shell
├── AI_GIT.md                 # 04: Git, GitHub, version control
│
└── telegram_tutorial/        # 05: Telegram bots (python-telegram-bot)
    ├── README.md
    ├── telegram_server.py
    └── telegram_test1.py … telegram_test7.py
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
