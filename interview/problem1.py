'''writ python program to conver sring "file_name_12012024_12132425"'''

string = "file_name_12012024_12132425"

def convert_string():
    parts = string.split("_")  # Split using '_'
    file_name = "_".join(parts[:2])  # Combine first two parts for file name
    date = parts[2]  # Extract the date
    timestamp = parts[3]  # Extract the timestamp
    return file_name, date, timestamp

# Call the function and display the result
file_name, date, timestamp = convert_string()
print(f"File Name: {file_name}")
print(f"Date: {date}")
print(f"Timestamp: {timestamp}")
