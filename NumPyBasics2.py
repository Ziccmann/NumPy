import pandas as pd

data = {
    'OrderID': [1, 2, 3, 4, 5],
    'ProductCategory': ['Electronics', 'Clothing', 'Books', 'Electronics', 'Clothing'],
    'Quantity': [2, 3, 1, 4, 2],
    'TransactionDate': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']
}

transactions = pd.DataFrame(data)

print("DataFrame - Transactions:")
print(transactions)