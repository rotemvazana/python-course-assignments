# Day 04: 

## Description
This assignment is an extended version of the Primer Tm Calculator program from day03.

A reminder:
This program calculates the melting temperature (Tm) of a DNA primer sequence entered by the user through 3 different interfaces: the `input()` function, the command line, and a Graphical User Interface (GUI).
The melting temperature is an important parameter in molecular biology, especially for designing primers for PCR experiments.

**What is new in this version?**

1. **GC content calculation and validation:** The program now calculates the GC percentage and verifies it falls within the optimal range (40-60%).

   Why 40-60%? Since G and C form 3 hydrogen bonds (compared to only 2 in A-T pairs), they provide greater stability to the primer-template complex.
   If the GC content is too low, the primer-template binding might be too weak, leading to failed amplification. If it is too high, the primer may bind
   non-specifically to other regions or form secondary structures (such as hairpins) that interfere with the PCR reaction.

2. **3' GC clamp detection:** The program now inspects the 3' end of the sequence to verify the presence of a "GC clamp".
   
   The 3' end of the primer is the most critical region because it is where the DNA polymerase binds and begins adding nucleotides. The 3' end of the primer should have 1-3 G/C bases within the last 5 nucleotides to ensure strong binding, known as a "GC clamp". However, we need to avoid more than 3 G/C bases at the 3' end to prevent non-specific annealing.

3. **Protection against empty inputs**: Following the suggestion of Stav Openhaimer, the program now returns an error message if the user submits an empty input.
   
4. **Removal of accidental spaces at the beginning/end of the sequence**: Implemented using the `strip()` method.   


## Work Summary
After extending the module as described above, I adjusted the 3 different user interface versions to fit the new version of the module. The same was done to the test file to ensure the new version works as expected.

*Additionally, I created a `.gitignore` file to exclude the `__pycache__` folder from the repository, ensuring a clean project environment.


## Files:
- `primer_tm_extended_module.py`  
  The core "business logic" containing all calculations.

- `tm_extended_input.py`  
  A version that interacts with the user using standard input (`input()`).

- `tm_extended_cmdline.py`  
  A command-line interface version that allows the user to enter the DNA sequence directly when running the program from the command line.

- `tm_extended_gui.py`  
  A graphical user interface (GUI) version built using `tkinter`, providing a user-friendly window for calculations.

- `test_tm_extended.py`  
  A test file that verifies the business logic using `pytest`.


## Requirements
This project uses **pytest** for automated testing. Since it is a third-party library, you may need to install it before running the tests:

pip install pytest

*I also created a requirements.txt file that includes it, so you can alternatively use:

pip install -r requirements.txt


## AI Usage
I used [Gemini](https://gemini.google.com/app) to assist with the following things:

prompts:
1. היי, אני רוצה להרחיב את הקוד הבא שמחשב את טמפרטורת ההתכה של פריימרים. אני רוצה שהקוד יבדוק גם האם אחוז ה-GC נמצא בטווח האופטימלי (40-60 אחוז) והאם יש GC clamp בקצה 3 או לא.
2. תוכל לעזור לי לעדכן את 3 הקודים הבאים (כל אחד מהם זו דרך שונה של המשתמש להכניס את האינפוט שלו) כדי שיתאימו לmodule החדש?
