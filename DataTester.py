import pandas as pd
import os
import matplotlib.pyplot as plt

# Path to the base directory
base_path = "C:\\Users\\Aweso\\Downloads\\The folder\\Data\\DB2\\DB2_s1"

# Creating the columns we want to transfer
columns = [f'emg{x}' for x in range(10)]
columns.extend(["restimulus", "rerepetition","exercise"])

time = []

for x in range (100000):
    time.append(x)

# Looping through all the files in DB1 and copying the subset to a new directory
for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.endswith(".csv"):
            full_file_path = os.path.join(root, file)
            #new_file_path = full_file_path.replace("DB1", "PreProc\\db1")


            #print(new_file_path)
            df = pd.read_csv(full_file_path)

            new_df = df[columns].copy()
            for x in range(10):
                new_df['adding'] += new_df[f'emg{x}']
            #print(new_df.corr())
            plt.plot(time, new_df['adding'][:len(time)])  # Adjust 'emg0' and 150 as needed
            plt.show()
            break
            #new_df.to_csv(new_file_path, index=False)




