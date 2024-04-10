# test.py

import pytest
import os

@pytest.mark.workflow
def test_output_files():
    """Test that expected output files were generated"""
    
    # List expected output files
    expected_files = [
        'results/sample1.csv',
        'results/sample2.csv',
        'summary.txt'
    ]
    
    # Check each expected file
    for file in expected_files:
        assert os.path.exists(file) == True
        
@pytest.mark.workflow        
def test_summary_content():
    """Test summary text"""
    
    # Load summary file
    with open('summary.txt') as f:
        content = f.read()
        
    # Check expected strings
    assert 'Sample1: Passed' in content
    assert 'Sample2: Passed' in content