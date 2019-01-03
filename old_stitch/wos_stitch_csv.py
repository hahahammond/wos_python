import pandas as pd
import os

root = 'data'

files = [f for f in os.listdir(root)]

merged = []

for f in files:
    if not f.startswith('.') and os.path.isfile(os.path.join(root, f)):
#        print(f)
#        print(os.path.isfile(os.path.join(root, f)))
        filename, ext = os.path.splitext(f)
        if ext == '.csv':
            print(f)
            read = pd.read_csv(os.path.join(root, f))
            merged.append(read)

result = pd.concat(merged)

result.to_csv('merged_csv.csv', index = False)
