def log_transaction(transaction_data):
    file = open("transaction_log.txt", 'a')  # Open file in append mode
    file.close()# Write transaction data to the file
    file.write(transaction_data)
# Example usage
transaction_data = "Transaction details: [Account: 123456, Amount: $100]"
log_transaction(transaction_data)
