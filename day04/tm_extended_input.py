from primer_tm_extended_module import calculate_tm

# Get primer sequence from user input
seq = input("Enter the primer sequence: ")
result, error = calculate_tm(seq)

if error:
    print(error)
else:
    print("-" * 30)
    print(f"Tm: {result['tm']:.2f}°C")
    print(f"Method: {result['method']}")
    print(f"Length: {result['length']} bp")
    print("-" * 30)
    # Display QC metrics: GC Content and GC Clamp
    print(f"GC Content: {result['gc_content']}% ({result['gc_status']})")
    print(f"GC Clamp: {result['clamp_status']}")
    print("-" * 30)