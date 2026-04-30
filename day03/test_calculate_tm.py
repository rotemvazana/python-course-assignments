# This program contains different tests to verify the "business logic" works as expected.
# Run this file using the 'pytest' command (pytest test_calculate_tm.py)

from primer_tm_module import calculate_tm

def test_short_primer():
    # Tests the Wallace formula for a sequence shorter than 14 bp
    # ATGC: 2*2(AT) + 2*4(GC) = 12
    result, error = calculate_tm("ATGC")
    assert error is None
    assert result['tm'] == 12
    assert result['method'] == "Short primer formula"

def test_long_primer():
    # Tests the formula for a sequence >= 14 bp
    # GATCGATCGATCGATCGATC (20 bp, GC count = 10)
    # Calculation: 64.9 + 41 * (10 - 16.4) / 20 = 51.78
    result, error = calculate_tm("GATCGATCGATCGATCGATC")
    assert error is None
    assert round(result['tm'], 2) == 51.78
    assert result['method'] == "Long primer formula"

def test_invalid_sequence():
    # Tests that an error is returned for non-DNA bases
    result, error = calculate_tm("GTTACCRGGATCTC")
    assert result is None
    assert "Error" in error
    assert "Invalid sequence" in error