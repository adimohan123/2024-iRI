import pandas as pd
import os
import matplotlib.pyplot as plt

# Path to the base directory
base_path = "C:\\Users\\Aweso\\Downloads\\The folder\\Data\\PreProc\\IOdb1"

# Creating the columns we want to transfer
# columns = [f'emg{x}' for x in range(10)]
# columns.extend(["restimulus", "rerepetition","exercise"])

BigD = pd.DataFrame()

# Looping through all the files in DB1 and copying the subset to a new directory
walk_generator = os.walk(base_path)

# Unpack the first tuple from the generator
root, dirs, files = next(walk_generator)

for file in files:
    if file.endswith(".csv"):
        full_file_path = os.path.join(root, file)

        # print(new_file_path)
        df = pd.read_csv(full_file_path)
        BigD = pd.concat([BigD, df])

BigD.drop_duplicates(inplace=True)
print(BigD)
print(len(BigD))
new_file_path = base_path.replace("PreProc\\IOdb1", "BigD1.csv")
BigD.to_csv(new_file_path, index=False)
