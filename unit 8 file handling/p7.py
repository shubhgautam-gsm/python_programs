# a append(add) new transaction and create new file if not available
def log_transaction(transaction_data):
    with open("transaction_log4.txt", 'a') as file:  # Open file in append mode
        file.write(transaction_data)

# Example usage
transaction_data = "Transaction details: [Account: e56, Amount: $100]"
log_transaction(transaction_data)
