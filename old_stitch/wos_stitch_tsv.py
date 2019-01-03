import pandas as pd
import os

root = 'data'

files = [f for f in os.listdir(root)]

merged = []

for f in files:
    if not f.startswith('.') and os.path.isfile(os.path.join(root, f)):
        filename, ext = os.path.splitext(f)
        if ext == '.tsv':
            print(f)
            read = pd.read_csv((os.path.join(root, f)), sep='\t', header=0)

            merged.append(read)

result = pd.concat(merged)

result.to_csv('merged_tsv.csv', index = False)
