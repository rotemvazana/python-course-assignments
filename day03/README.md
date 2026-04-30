# Day 03: 

## Description
This assignment is a continuation of the Primer Tm Calculator program from day02.

A reminder:
This program calculates the melting temperature (Tm) of a DNA primer sequence entered by the user.
The melting temperature is an important parameter in molecular biology, especially for designing primers for PCR experiments.
More detailed information can be found on the README.md file found in day02 folder.


## Work Summary
First, I copied the program from day02 into the day03 folder (under the name: `primer_tm_calc_solution_from_day02.py`).

Then, I converted the "business logic" (the computation) into a function and moved it to a separate file (`primer_tm_module.py`).

Next, I created three different versions of the program, each using the shared module but providing a different way for the user to interact with it:
- Standard input (using the `input()` function)
- Command-line (using `sys.argv`)
- Graphical User Interface (GUI) using tkinter

Finally, I created a test file with several test cases to verify that the business logic works as expected.


## Files:
- `primer_tm_module.py`  
  Contains the core computation logic (business logic) for calculating the melting temperature (Tm).

- `primer_tm_input.py`  
  A version that interacts with the user using standard input (`input()`).

- `primer"_tm_cmdline.py`  
  A command-line interface version that allows the user to enter the DNA sequence directly when running the program from the command line..

- `primer_tm_gui.py`  
  A graphical user interface (GUI) version built using `tkinter`, providing a user-friendly window for calculations.

- `test_calculate_tm.py`  
  A test file that verifies the business logic using `pytest`.


## Requirements
This project uses **pytest** for automated testing. Since it is a third-party library, you may need to install it before running the tests:

pip install pytest


## AI Usage
I used [Gemini](https://gemini.google.com/app) to assist with the following things:

prompts:
1. היי, תוכל לעזור לי להפוך את החישוב של טמפרטורת ההתכה (ה-"business logic") לפונקציה?
2. הפרדתי את הפונקציה מהממשק עם הuser, תוכל לעזור לי לכתוב קוד עבור הממשק הגרפי GUI תוך שימוש בספריית tinker?
3. על בסיס הקוד של הפונקציה שלי, איזה מבחנים כדאי לי להריץ כדי לוודא שהיא עובדת כראוי? 


