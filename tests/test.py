import pytest
import os

# Define the tests
def test_output_files():
    """Test that expected output files were generated"""
    
    # List expected output files
    expected_files = [
        'results/sample1.csv',
        'results/sample2.csv',
        'results/summary.txt'
    ]
    
    # Check each expected file
    for file in expected_files:
        # Get the absolute path to the file based on the current directory
        file_path = os.path.abspath(file)
        assert os.path.exists(file_path)  # Check if the file exists

@pytest.mark.workflow
def test_summary_content():
    """Test summary text"""
    
    # Define the path to summary.txt based on your repository structure
    summary_path = 'results/summary.txt'
    
    # Load summary file
    with open(summary_path) as f:
        content = f.read()

    # Check expected strings based on the actual content (including tabs and spaces)
    expected_content = 'Sample\tStatus\nSample1\tPassed\nSample2\tPassed'
    assert expected_content == content.strip()  # Strip any leading or trailing whitespace

