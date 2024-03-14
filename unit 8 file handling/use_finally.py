def process_file(filename):
    try:
        fileptr = open(filename, "r")  # Open the file in read mode
        try:
            # Perform file operations
            if fileptr:
                print("File is opened successfully")
                file_content = fileptr.read()
                print("Content of", filename, ":")
                print(file_content)
                # Perform some processing
                1 / 0  # Simulate an error during processing
        finally:
            fileptr.close()  # Close the file in the finally block
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred during processing:", str(e))
# Example usage:
process_file("file.txt")
