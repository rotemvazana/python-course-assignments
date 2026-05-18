import pytest
import pandas as pd
import numpy as np
from analysis import analyze_protocol_efficiency  # Importing the function from your main script

def test_protein_counting_with_nans(tmp_path):
    """
    Test that the code accurately counts identified proteins per sample
    and handles missing values (NaNs) by ignoring them in the count.
    """
    # Create a temporary Excel file in a virtual directory for the test
    file_path = tmp_path / "test_data.xlsx"
    
    # Mock data structure:
    # Protein 1: detected in both S1 and S2
    # Protein 2: detected only in S1 (contains NaN in S2)
    pd.DataFrame([
        {"Protein.Group": "P1", "Genes": "GeneA", "S1": 500, "S2": 1200},
        {"Protein.Group": "P2", "Genes": "GeneB", "S1": 350, "S2": np.nan}
    ]).to_excel(file_path, index=False)
    
    # Define dummy sample groups for testing
    group_a = ["S1"]
    group_b = ["S2"]
    
    # Run the main processing function
    summary_df = analyze_protocol_efficiency(str(file_path), group_a, group_b)
    
    # Verify that exactly two rows were generated (one row per sample)
    assert len(summary_df) == 2
    
    # Extract calculated protein counts 
    s1_count = summary_df.loc[summary_df['Protocol'] == 'Lab Protocol (50 cells, n=5)', 'Protein_Count'].values[0]
    s2_count = summary_df.loc[summary_df['Protocol'] == 'Other Protocol (100 cells, n=2)', 'Protein_Count'].values[0]
    
    # S1 should have 2 proteins, S2 should have only 1 protein
    assert s1_count == 2
    assert s2_count == 1


def test_ignore_zero_and_negative_intensities(tmp_path):
    """
    Test that the logic treats an intensity of 0 or a negative value 
    as 'Not Detected' and excludes them from the protein count.
    """
    file_path = tmp_path / "test_zeros.xlsx"
    
    # Mock data with invalid intensities:
    # Protein 1 has 0 intensity in S1 (should be ignored)
    # Protein 2 has a negative artifact intensity in S1 (should be ignored)
    pd.DataFrame([
        {"Protein.Group": "P1", "Genes": "GeneA", "S1": 0, "S2": 800},
        {"Protein.Group": "P2", "Genes": "GeneB", "S1": -5, "S2": 400}
    ]).to_excel(file_path, index=False)
    
    summary_df = analyze_protocol_efficiency(str(file_path), ["S1"], ["S2"])
    
    s1_count = summary_df.loc[summary_df['Protocol'] == 'Lab Protocol (50 cells, n=5)', 'Protein_Count'].values[0]
    s2_count = summary_df.loc[summary_df['Protocol'] == 'Other Protocol (100 cells, n=2)', 'Protein_Count'].values[0]
    
    # S1 has no valid proteins (0 and -5), so the count must be 0
    assert s1_count == 0
    # S2 has two valid proteins (> 0), so the count must be 2
    assert s2_count == 2


def test_missing_gene_names_fallback(tmp_path):
    """
    Test that if a Gene name is missing (NaN), the code safely falls back 
    to the Protein.Group ID instead and does not crash during execution.
    """
    file_path = tmp_path / "test_fallback.xlsx"
    
    # Row 2 contains a missing Gene name but has a valid Protein.Group ID
    pd.DataFrame([
        {"Protein.Group": "P1", "Genes": "GeneA", "S1": 400},
        {"Protein.Group": "ProteinGroup_X", "Genes": np.nan, "S1": 600}
    ]).to_excel(file_path, index=False)
    
    # Verify that the function runs and aggregates safely without raising exceptions
    try:
        summary_df = analyze_protocol_efficiency(str(file_path), ["S1"], [])
        s1_count = summary_df.loc[summary_df['Protocol'] == 'Lab Protocol (50 cells, n=5)', 'Protein_Count'].values[0]
        # Both rows should be successfully counted
        assert s1_count == 2
    except Exception as e:
        pytest.fail(f"The analysis function crashed due to a missing gene name: {e}")