import os

def print_directory_contents(path):
    try:
        # List all files and directories in the given path
        contents = os.listdir(path)
        print(f"Contents of '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except NotADirectoryError:
        print(f"'{path}' is not a directory.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")

# Example usage
directory_path = "/home/akshay/Desktop"
print_directory_contents(directory_path)
