# w write(update) old transaction and create new file if not available
def log_transaction(transaction_data):
    with open("transaction_log4.txt", 'r') as file:  #file cannot write if we want because 'r'
        file.write(transaction_data)                 #not 'w'(write)

# Example usage
transaction_data = "Transaction details: [Account: 556, Amount: $100]"
log_transaction(transaction_data)
