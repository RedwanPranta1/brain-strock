# In DecisionTree.py

import pandas as pd

def process(df, input_1, input_2):
    try:
        # Example processing: adding a new column based on input parameters
        df['new_column'] = df['existing_column'] * int(input_2)  # Example logic
        return df
    except Exception as e:
        raise RuntimeError(f"Error in processing: {e}")
