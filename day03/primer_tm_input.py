from primer_tm_module import calculate_tm

seq = input("Enter the primer sequence: ")
result, error = calculate_tm(seq)

if error:
    print(error)
else:
    print(f"Tm: {result['tm']:.2f}°C using {result['method']}")