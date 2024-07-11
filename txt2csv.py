import csv


def txt_to_csv(txt_file_path, csv_file_path, delimiter='\t'):
    with open(txt_file_path, 'r') as txt_file:
        reader = csv.reader(txt_file, delimiter=delimiter)

        with open(csv_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for row in reader:
                writer.writerow(row)


# Example usage
txt_file_path = 'C:\\Users\\Aweso\\Downloads\\The folder\\Backup\\Filtered Data\\001\\task_1.txt'
csv_file_path = 'C:\\Users\\Aweso\\Downloads\\The folder\\Backup\\Filtered Data\\001\\task_1.csv'
delimiter = '\t'  # Change this if your txt file uses a different delimiter
txt_to_csv(txt_file_path, csv_file_path, delimiter)
