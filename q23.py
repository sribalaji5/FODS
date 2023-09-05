import pandas as pd

data = {
    'Product': ['A', 'B', 'C', 'D'],
    'Price': [10, 15, 20, 25],
    'Quantity': [100, 80, 60, 40]
}

df = pd.DataFrame(data)
df['Total'] = df['Price'] * df['Quantity']
total_sales = df['Total'].sum()

print(f'Total sales: ${total_sales}')
