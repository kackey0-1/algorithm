import pandas as pd


if __name__ == '__main__':
    # Load data
    sales = pd.read_csv('uriage.csv')
    customer = pd.read_excel('kokyaku_daicho.xlsx')

    print(sales.head())
    print('#'*10)
    print(customer.head())
    print('#'*10)
