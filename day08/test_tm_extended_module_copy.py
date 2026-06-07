# This program contains different tests to verify that the "business logic" works as expected.
# Run this file using the 'pytest' command (pytest test_tm_extended.py).

from tm_extended_module_copy import calculate_tm

def test_short_primer():
    # Tests the Wallace formula and GC Content for a short sequence
    # ATGC: 2*2(AT) + 2*4(GC) = 12. GC Content: 2/4 = 50%
    result, error = calculate_tm("ATGC")
    assert error is None
    assert result['tm'] == 12
    assert result['gc_content'] == 50.0
    assert result['gc_status'] == "Optimal"
    assert result['method'] == "Short primer formula"

def test_long_primer():
    # Tests the formula for a sequence >= 14 bp
    # GATCGATCGATCGATCGATC (20 bp, GC count = 10)
    # Calculation: 64.9 + 41 * (10 - 16.4) / 20 = 51.78. GC Content: 10/20 = 50%
    result, error = calculate_tm("GATCGATCGATCGATCGATC")
    assert error is None
    assert round(result['tm'], 2) == 51.78
    assert result['gc_content'] == 50.0
    assert result['gc_status'] == "Optimal"
    assert result['method'] == "Long primer formula"

def test_gc_clamp_and_status():
    # Tests GC Clamp and GC Content boundaries
    # AAAAAA (6 bp, GC count = 0)
    result, error = calculate_tm("AAAAAA")
    assert error is None
    assert result['gc_content'] == 0.0
    assert result['gc_status'] == "Warning: Outside 40-60% range"
    assert result['gc_clamp'] is False
    assert "Suboptimal" in result['clamp_status']

    # GCGCAAAAAA (10 bp, GC count = 4, No clamp at 3' end)
    result, error = calculate_tm("GCGCAAAAAA")
    assert result['gc_clamp'] is False  # Last 5 bases are AAAAA
    
    # AAAAAGCG (8 bp, GC count = 3, Has clamp at 3' end)
    result, error = calculate_tm("AAAAAGCG")
    assert result['gc_clamp'] is True  # Last 5 bases are AAGCG (3 G/C bases)

def test_invalid_sequence():
    # Tests that an error is returned for non-DNA bases
    result, error = calculate_tm("GTTACCRGGATCTC")
    assert result is None
    assert "Error" in error
    assert "Invalid sequence" in error

def test_empty_sequence():
    # Tests that an empty string returns an appropriate error
    result, error = calculate_tm("")
    assert result is None
    assert "empty" in error.lower()