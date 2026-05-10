# This program allows the user to input the primer sequence via the command line
import sys
from primer_tm_extended_module import calculate_tm

if len(sys.argv) < 2:
    print(f"Usage: python {sys.argv[0]} <put your sequence here>")
    print(f"Example: python {sys.argv[0]} GATCGATCGATCGATCGATC")
else:
    # Get sequence from the first argument
    seq = sys.argv[1]
    result, error = calculate_tm(seq)
    
    if error:
        print(error)
    else:
        print("-" * 30)
        print(f"Primer Analysis for: {seq}")
        print(f"Length: {result['length']} bp")
        print(f"Tm: {result['tm']:.2f}°C ({result['method']})")
        print("-" * 30)
        
        # Display Quality Control (QC) metrics
        print(f"GC Content: {result['gc_content']}% ({result['gc_status']})")
        print(f"GC Clamp: {result['clamp_status']}")
        print("-" * 30)