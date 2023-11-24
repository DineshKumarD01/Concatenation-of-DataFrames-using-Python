#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[10]:


def merge_csv_files(file1_path, file2_path, output_path):
    # Read CSV files into pandas DataFrames
    df1 = pd.read_csv(file1_path, header=None)
    df2 = pd.read_csv(file2_path, header=None)

    # Merge DataFrames based on the first column, using a left join
    merged_df = pd.merge(df1, df2, left_on=df1.columns[0], right_on=df2.columns[0], how='left')

    # Drop the duplicate column from CSV2
    merged_df = merged_df.drop(columns=[df2.columns[0]])

    # Write the result to an output file without header
    merged_df.to_csv(output_path, index=False, header=False)
    
# Example usage
merge_csv_files('1.csv', '2.csv', 'output_file.csv')


# In[ ]:





# In[ ]:





# In[ ]:




