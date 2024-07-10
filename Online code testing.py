import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

# Path to the base directory
base_path = "C:\\Users\\Aweso\\Downloads\\The folder\\Data\\PreProc\\db1"

# Creating the columns we want to transfer
columns = [f'emg{x}' for x in range(10)]
columns.extend(["restimulus", "rerepetition", "exercise"])

# Looping through all the files in DB1 and copying the subset to a new directory
for root, dirs, files in os.walk(base_path):
    for file in files:

        if file.endswith(".csv"):
            full_file_path = os.path.join(root, file)
            new_file_path = full_file_path.replace("db1", "IOdb1")

            print(new_file_path)
            df = pd.read_csv(full_file_path)  # reading from the preprocced dataset
            new_df = pd.DataFrame(columns=columns)
            new_df['Ex+Sti+Rep'] = []

            if 'E1' in file:
                index = 120
                ex = '1'
            elif 'E2' in file:
                index = 170
                ex='2'
            else:
                index = 230
                ex='3'



            for indx in range(index):
                # established correct repition(10) and index (12)
                re = indx % 10 +1
                if indx < 10:
                    stim = 1
                elif indx < 100:
                    stim = int(str(indx)[:1]) +1
                else:
                    stim = int(str(indx)[:2]) +1

                filtered_df = pd.DataFrame() # hopefully clear the memory

                filtered_df = df[(df['restimulus'] == stim) & (df['rerepetition'] == re)]

                REP = {}  # holds all the 10 sets of EMG values
                for i in range(0, 10):
                    REP[f'emgIN{i}'] = []

                for index, row in filtered_df.iterrows():  # Taking the colums and putting it in vector
                    for x in range(0, 10):
                        REP[f'emgIN{x}'].append(row[f'emg{x}'])

                # putting the Lists into the rows
                new_df.loc[indx] = [REP['emgIN0'], REP['emgIN1'], REP['emgIN2'],
                                    REP['emgIN3'], REP['emgIN4'], REP['emgIN5'], REP['emgIN6'],
                                    REP['emgIN7'], REP['emgIN8'], REP['emgIN9'], stim, re,
                                    ex,ex + '_' + str(stim) +'_'+ str(re)]  # Stim #rep #excercise #label








        # deleting unessassary things
        del new_df['restimulus']
        del new_df['exercise']
        del new_df['rerepetition']

        new_df.to_csv(new_file_path, index=False)

    # for index, row in new_df.iterrows():
    #  print(f"Index: {index}")
    # print(f"Vector in column A: {row['emg0']}")
    # print(f"Vector in column B: {row['1']}")
