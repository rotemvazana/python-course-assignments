# Primer Tm Calculator

## Program Description
This program calculates the melting temperature (Tm) of a DNA primer sequence entered by the user.
The melting temperature is an important parameter in molecular biology, especially for designing primers for PCR experiments.

The program automatically selects the appropriate formula based on the primer length:

1. **Short Primers (< 14 bp):** Uses the **(Wallace Formula)**
   $T_m = (#A+#T) \times 2 + (#G+#C) \times 4$
2. **Long Primers (≥ 14 bp):** Uses a more accurate empirical formula
   $T_m = 64.9 + \frac{41 \times (#G+#C - 16.4)}{(#A+#T+#G+#C)}$

## Notes
*The program validates that the input sequence contains only valid DNA nucleotides (A, T, C, G) and does not include any unintended characters
that may have been entered by mistake by the user.

*If invalid characters (e.g. the letter R or a number) are detected, the program will display an error message.

## Sample Inputs for Testing
1. **Input Sequence:** GATCGATCGATCGATCGATC 
* **Expected Output:**
  * Sequence: GATCGATCGATCGATCGATC
  * Length: 20 bp
  * Method: long primer formula
  * Calculated Tm: 51.78°C
 
2. **Input Sequence:** GTTACCRGGATCTC
* **Expected Output:** an error message:
  Error: Invalid sequence! Please use only A, T, C, and G.
  

## AI Usage
