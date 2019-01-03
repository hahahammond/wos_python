# Script to stitch together Web of Science tsv search results files and find duplicate values 

import pandas as pd
import os

# Define text file stitch function
def stitch(root):
    files = [f for f in os.listdir(root)]
    merged = []
    
    for f in files:
        if not f.startswith('.') and os.path.isfile(os.path.join(root, f)):
            filename, ext = os.path.splitext(f)
            if ext == '.txt':
                read = pd.read_csv((os.path.join(root, f)),  sep='\t', index_col=False)
                merged.append(read)
    
    result = pd.concat(merged)
    return result
    
# Stitch together tsv files
pubs =  stitch('input_files')

# Find missing data
# Tutorial: https://dzone.com/articles/pandas-find-rows-where-columnfield-is-null
pubs.isnull().any()
pubs.UT.isnull().any()
null_columns=pubs.columns[pubs.isnull().any()]
pubs[null_columns].isnull().sum()

# Count unique values by df column
len(pubs.UT.unique())
len(pubs.AU.unique())

# Find duplicate author/ title  / publication rows
# List of Web of Science Field Tag codes: http://images.webofknowledge.com.ezproxy.bu.edu//WOKRS531NR4/help/WOS/hs_wos_fieldtags.html
pubs.duplicated(subset=['AU', 'TI'], keep=False)
dupe_au_ti_so= pubs[pubs.duplicated(subset=['AU', 'TI', 'SO'], keep=False)]
dupe_au_ti = pubs[pubs.duplicated(subset=['AU', 'TI'], keep=False)]
dupe_au = pubs[pubs.duplicated(subset=['AU'], keep=False)]
dupe_ti = pubs[pubs.duplicated(subset=['TI'], keep=False)]

# Output CSVs
pubs.to_csv('output_files/pubs.csv', index=False)
pubs.PM.dropna().to_csv('output_files/pubs_pmids.csv', index=False)
pubs.UT.dropna().to_csv('output_files/pubs_wos_nums.csv', index=False)
dupe_au_ti_so.to_csv('output_files/dupe_au_ti_so.csv', index=False)
dupe_au_ti.to_csv('output_files/dupe_au_ti.csv', index=False)
dupe_au.to_csv('output_files/dupe_au.csv', index=False)
dupe_ti.to_csv('output_files/dupe_ti.csv', index=False)
