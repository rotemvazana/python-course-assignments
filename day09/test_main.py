import pytest
import pandas as pd
from main import load_data, preprocess_data

def test_load_data_file_not_found():
    """Test that loading a non-existent file raises a FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        load_data('fake_non_existent_file.csv')

def test_preprocess_data_target_missing():
    """Test that preprocessing raises a ValueError if target column is missing."""
    # Create a mock dataframe without the LUNG_CANCER column
    mock_df = pd.DataFrame({'AGE': [50, 60], 'SMOKING': [1, 2]})
    
    with pytest.raises(ValueError):
        preprocess_data(mock_df, target_col='LUNG_CANCER')

def test_preprocess_data_encoding():
    """Test that the target is binarized and categorical columns are one-hot encoded."""
    # Create a mock dataframe with mixed data types
    mock_df = pd.DataFrame({
        'AGE': [50, 60], 
        'SMOKING': [1, 2],
        'GENDER': ['M', 'F'], # Text column
        'LUNG_CANCER': ['YES', 'NO'] # Target text column
    })
    
    X, y, le = preprocess_data(mock_df, target_col='LUNG_CANCER')
    
    # 1. Verify target encoding (YES should be 1, NO should be 0 based on alphabetical order)
    # The LabelEncoder sorts classes, so NO=0, YES=1
    assert list(y) == [1, 0] 
    
    # 2. Verify One-Hot Encoding happened properly on X
    assert 'GENDER' not in X.columns # Original column should be gone
    assert 'GENDER_M' in X.columns # Dummy column should be created (dropping first usually drops F)
    
    # 3. Verify numerical columns remained intact
    assert 'AGE' in X.columns
    assert 'SMOKING' in X.columns