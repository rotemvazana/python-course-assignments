# This program uses a Graphical User Interface (GUI) for the Primer Tm Calculator.
# It provides Tm calculations along with GC Content and GC Clamp quality checks.

import tkinter as tk
from tkinter import messagebox
from primer_tm_extended_module import calculate_tm

def run_calc():
    # Get sequence from the input field and remove leading/trailing spaces
    seq = entry.get().strip()
    
    # Check if the input is empty
    if not seq:
        messagebox.showwarning("Input Error", "Please enter a DNA sequence.")
        return

    # Call the business logic from the module
    result, error = calculate_tm(seq)
    
    if error:
        # Show error message if the sequence is invalid
        messagebox.showerror("Error", error)
    else:
        # Build a detailed output string with the new QC metrics
        output = (
            f"Tm: {result['tm']:.2f}°C\n"
            f"Method: {result['method']}\n"
            f"Length: {result['length']} bp\n"
            f"{'-'*25}\n"
            f"GC Content: {result['gc_content']}% ({result['gc_status']})\n"
            f"GC Clamp: {result['clamp_status']}"
        )
        
        # Update the result label with the formatted text
        label_res.config(text=output, fg="black")

# Initialize the main application window
root = tk.Tk()
root.title("Primer Quality Calculator")
root.geometry("350x320")  # Adjusted size to fit all the information

# UI Elements
tk.Label(root, text="Enter Primer Sequence:", font=("Arial", 10, "bold")).pack(pady=5)

entry = tk.Entry(root, width=35)
entry.pack(pady=5)

# Calculate Button with a slightly different background color for better visibility
tk.Button(root, text="Calculate", command=run_calc, bg="#e1e1e1", width=15).pack(pady=10)

# Result area - using a monospaced font (Courier) for a clean, aligned look
label_res = tk.Label(root, text="", justify="left", font=("Courier", 10))
label_res.pack(pady=10)

# Start the GUI event loop
root.mainloop()