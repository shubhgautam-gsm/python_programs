def log_transaction(transaction_data):
    with open("transaction_log.txt", 'a') as file:  # Open file in append mode
        file.write(transaction_data)

# Example usage
transaction_data = "Transaction details: [Account: 123456, Amount: $100]"
log_transaction(transaction_data)
