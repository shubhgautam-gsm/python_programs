# w write(update) old transaction and create new file if not available
def log_transaction(transaction_data):
    with open("transaction_log4.txt", 'w') as file:  # Open file in append mode
        file.write(transaction_data)

# Example usage
transaction_data = "Transaction details: [Account: 556, Amount: $100]"
log_transaction(transaction_data)
