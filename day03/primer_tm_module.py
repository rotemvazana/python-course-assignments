# This program contains only the "business logic" (the computations)
# It is designed to be imported as a module by other scripts.

def calculate_tm(sequence):
    sequence = sequence.upper()
    length = len(sequence)
    
    # Counting valid nucleotides
    count_a = sequence.count('A')
    count_t = sequence.count('T')
    count_c = sequence.count('C')
    count_g = sequence.count('G')

    # Validation: Check if the sum of valid bases equals the total length
    if (count_a + count_t + count_c + count_g) != length:
        return None, "Error: Invalid sequence! please Use only A, T, C, G."

    count_at = count_a + count_t
    count_gc = count_c + count_g

    # Choosing the formula
    if length < 14:
        # Wallace Formula for short primers
        tm = (count_at * 2) + (count_gc * 4)
        method = "Short primer formula"
    else:
        # formula for longer primers
        tm = 64.9 + 41 * (count_gc - 16.4) / length
        method = "Long primer formula"
        
    return {"tm": tm, "method": method, "length": length}, None