import os
import pandas as pd

folder_path = r'./test_excel'

files = [file for file in os.listdir(folder_path) if file.endswith('.xlsx') and file.startswith('ac')]

all_data = pd.DataFrame()

for file in files:
    file_path = os.path.join(folder_path, file)
    if os.path.exists(file_path):
        print(file_path)
        df = pd.read_excel(file_path)
        all_data = pd.concat([all_data, df], ignore_index=True)
    else:
        print(f"File not found: {file_path}")   

print(all_data)