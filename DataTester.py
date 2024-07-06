import pandas as pd

# Replace 'your_file.csv' with the path to your CSV file
csv_file = # I will need code to cycle through this

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file)

# Initialize a dictionary to store counts of data points for each column
data_points_count = {}

# Iterate over the specified columns (emg[0] to emg[9])
for i in range(10):
    column_name = f'emg{i}'
    if column_name in df.columns:
        # Count the number of non-null data points in the column
        count = df[column_name].count()
        data_points_count[column_name] = count
    else:
        data_points_count[column_name] = 0

# Print the results
for column, count in data_points_count.items():
    print(f'{column}: {count} data points')
