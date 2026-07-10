# pythonteaching
Contains Python teaching materials.
This git repo does NOT contain any solutions to the questions. It only includes lecture notes and questions.

# Requirements
- Python 3.9+ (standard library only; the 2048 game uses tkinter, which ships with most Python installations)

# Running the materials
- Homework/lecture files are skeletons — fill in the `"*** YOUR CODE HERE ***"` sections, then check your work with the built-in doctests:
  ```
  python3 -m doctest src/hw1/hw01.py -v
  ```
- 2048 game (after implementing the functions in `logic.py`):
  ```
  cd src/2048 && python3 puzzle.py
  ```
  Controls: WASD or the arrow keys.

# lec, hw folder
- py file: Students will edit this file to reach the correct solution 
- The homework solution will not be posted to avoid potential academic dishonesty in cs61a.
  
# Course Syllabus.pdf
- Contains information about the course flow.

# 2048
- Inspired from Tay Yang Shun, Emmanuel Goh.
- A Python version of a famous puzzle game, 2048.
- Made some modifications to the file, so that the student could implement themselves and reach the final product.

# practice folder
- Contains extra Practice problems and solutions.

# Sources
- The Course Plan / Homework Problem Sets was inspired by John Denero and Paul Hilfinger from the Computer Science Department in UC Berkeley, cs61a.org.
- The Project, ‘2048’ was inspired from Tay Yang Shun, “https://github.com/yangshun/2048-python.

# Copyright
Author: Hyun Jae Moon
B.S. Electrical Engineering & Computer Science
University of California, Berkeley
hyunjaemoon@berkeley.edu
