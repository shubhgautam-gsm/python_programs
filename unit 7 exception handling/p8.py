def critical_operation(data):
    if not data:
        raise ValueError("Data cannot be empty!")
    # Perform the critical operation here

try:
    data = None  # Simulating empty data
    critical_operation(data)
    print("Critical operation completed successfully.")
except ValueError as e:
    print("An error occurred:", e)
    # Handle the error or perform cleanup tasks



# def critical_operation(data):
#     if not data:
#         print("Data cannot be empty!")
#     # Perform the critical operation here

# try:
#     data = None  # Simulating empty data
#     critical_operation(data)
#     print("Critical operation completed successfully.")
# except ValueError as e:
#     print("An error occurred:", e)
#     # Handle the error or perform cleanup tasks
