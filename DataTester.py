import pandas as pd
import matplotlib.pyplot as plt


# Need help with cycling through files
df = pd.read_csv("C:\\Users\\Aweso\\Downloads\\The folder\\Data\\DB1\\S9_A1_E2.csv")
#1218 is the # of data rows corresponding to the 3 second of rest at the begining
columns = []
for x in range(10):
    columns.append(f'emg{x}')
time = list(range(1218))

columns.append("restimulus")
new_df = df[columns]
first_150 = df['emg6'].head(1218)

print(new_df.corr())
print(new_df['emg6'].max())
plt.plot(time,first_150)
plt.show()


