def process_file_without_finally(filename):
    try:
        fileptr = open(filename, "r")  # Open the file in read mode
        # Perform file operations
        if fileptr:
            print("File is opened successfully")
            file_content = fileptr.read()
            print("Content of", filename, ":")
            print(file_content)
            # Simulate an error during processing
            1 / 0
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred during processing:", str(e))

# Example usage:
process_file_without_finally("file.txt")
