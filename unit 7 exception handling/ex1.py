def calculate_tax(income):
    if income < 0:
        raise ValueError("Income cannot be negative!")
        raise TypeError("Income cannot be negative!")
    # Perform tax calculation here

try:
    income = 'a' # Simulating negative income
    calculate_tax(income)
    print("Tax calculation completed successfully.")
except ValueError as e:
    print("An error occurred:", e)
    # Handle the error or perform cleanup tasks
except TypeError as e:
    print("An error occurred:", e)
