# generate_test_data.py

import pandas as pd
import random

# Generate sample results files 
for i in range(1, 3):
    data = {'Metric': [f'Metric{j}' for j in range(5)],
            'Value': [random.randint(0, 100) for _ in range(5)]}
    df = pd.DataFrame(data)
    df.to_csv(f'results/sample{i}.csv', index=False)

# Generate summary file
summary_data = {'Sample': ['Sample1', 'Sample2'],
                'Status': ['Passed', 'Passed']}
summary_df = pd.DataFrame(summary_data)
summary_df.to_csv('results/summary.txt', sep='\t', index=False)
