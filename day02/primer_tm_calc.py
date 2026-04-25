# Primer Melting Temperature (Tm) Calculator
# This program chooses the formula based on the primer length and calculates its Tm.

print("--- Primer Tm Calculator ---")

# Getting the sequence from the user
sequence = input("Enter the primer sequence: ").upper()
length = len(sequence)

# Counting valid nucleotides
count_a = sequence.count('A')
count_t = sequence.count('T')
count_c = sequence.count('C')
count_g = sequence.count('G')

# Validation: Check if the sum of valid bases equals the total length
if (count_a + count_t + count_c + count_g) != length:
    print("-" * 30)
    print("Error: Invalid sequence! Please use only A, T, C, and G.")
else:
    # If the sequence is valid, proceed with calculations
    count_at = count_a + count_t
    count_gc = count_c + count_g

    # Choosing the formula
    if length < 14:
        # Wallace Formula for short primers
        tm = (count_at * 2) + (count_gc * 4)
        formula_used = "short primer formula (Wallace Formula)"
    else:
        # formula for longer primers
        tm = 64.9 + 41 * (count_gc - 16.4) / (count_at + count_gc)
        formula_used = "long primer formula"

    print("-" * 30)
    print(f"Sequence: {sequence}")
    print(f"Length: {length} bp")
    print(f"Method: {formula_used}")
    print(f"Calculated Tm: {tm:.2f}°C")