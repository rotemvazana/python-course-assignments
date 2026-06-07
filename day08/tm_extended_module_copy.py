# This program contains the "business logic" (the computations) for day04.
# It calculates Tm and adds QC checks: GC Content and GC Clamp.

def calculate_tm(sequence):
    sequence = sequence.upper().strip()
    length = len(sequence)
    
    if length == 0:
        return None, "Error: Sequence is empty."

    # Counting valid nucleotides
    count_a = sequence.count('A')
    count_t = sequence.count('T')
    count_c = sequence.count('C')
    count_g = sequence.count('G')

    # Validation: Check if the sum of valid bases equals the total length
    if (count_a + count_t + count_c + count_g) != length:
        return None, "Error: Invalid sequence! Please use only A, T, C, G."

    count_at = count_a + count_t
    count_gc = count_c + count_g

    # 1. Tm Calculation
    if length < 14:
        # Wallace Formula for short primers
        tm = (count_at * 2) + (count_gc * 4)
        method = "Short primer formula"
    else:
        # Formula for longer primers
        tm = 64.9 + 41 * (count_gc - 16.4) / length
        method = "Long primer formula"

    # 2. GC Content Calculation and Validation (Target: 40-60%)
    gc_content = (count_gc / length) * 100
    is_gc_valid = 40 <= gc_content <= 60
    gc_status = "Optimal" if is_gc_valid else "Warning: Outside 40-60% range"

    # 3. GC Clamp Check (Looking at the last 5 bases at the 3' end)
    # A good clamp typically has 1-3 G/C bases to ensure stable binding.
    last_5 = sequence[-5:]
    clamp_gc_count = last_5.count('G') + last_5.count('C')
    has_clamp = 1 <= clamp_gc_count <= 3
    clamp_status = "Good" if has_clamp else "Suboptimal (Too many or too few G/C)"

    # Preparing the response dictionary
    result = {
        "tm": round(tm, 2),
        "method": method,
        "length": length,
        "gc_content": round(gc_content, 2),
        "gc_status": gc_status,
        "gc_clamp": has_clamp,
        "clamp_status": clamp_status
    }
        
    return result, None