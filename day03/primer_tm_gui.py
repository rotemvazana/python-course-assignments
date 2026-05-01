# This program uses a Graphical User Interface (GUI) for the Primer Tm Calculator.
# This interface allows users to enter their primer sequence without using the terminal.

import tkinter as tk
from tkinter import messagebox
from primer_tm_module import calculate_tm

def run_calc():
    seq = entry.get()
    result, error = calculate_tm(seq)
    if error:
        messagebox.showerror("Error", error)
    else:
        label_res.config(text=f"Tm: {result['tm']:.2f}°C\n({result['method']})")

root = tk.Tk()
root.title("Primer Tm Calc")
root.geometry("300x200")

tk.Label(root, text="Enter Sequence:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Calculate", command=run_calc).pack(pady=10)
label_res = tk.Label(root, text="")
label_res.pack(pady=5)

root.mainloop()