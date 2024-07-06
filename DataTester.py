import pandas as pd


# Need help with cycling through files
csv_file =

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file)


data_points_count = {}


for i in range(10):
    column_name = f'emg{i}'
    if column_name in df.columns:

        count = df[column_name].count()
        data_points_count[column_name] = count
    else:
        data_points_count[column_name] = 0

# Print the results
for column, count in data_points_count.items():
    print(f'{column}: {count} data points')
