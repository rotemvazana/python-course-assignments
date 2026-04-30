# This proogram allows the user to input the primer sequence via the command line

import sys
from primer_tm_module import calculate_tm

if len(sys.argv) < 2:
    print(f"Usage: python {sys.argv[0]} <put your sequence here>")
    print(f"Example: python {sys.argv[0]} GATCGATCGATCGATCGATC")
else:
    seq = sys.argv[1]
    result, error = calculate_tm(seq)
    if error:
        print(error)
    else:
        print(f"Tm: {result['tm']:.2f}°C using {result['method']}")