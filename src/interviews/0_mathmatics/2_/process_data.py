import pandas as pd


if __name__ == '__main__':
    # Load data
    sales = pd.read_csv('uriage.csv')
    customer = pd.read_excel('kokyaku_daicho.xlsx')

    print(sales.head())
    print('#' * 10)
    print(customer.head())
    print('#' * 10)
    print(sales['item_name'].head())
    print(sales['item_price'].head())
    print(customer['登録日'].head())
    print('#' * 10)

    # Aggregate data
    sales['purchase_date'] = pd.to_datetime(sales['purchase_date'])
    sales['purchase_month'] = sales['purchase_date'].dt.strftime('%Y%m')
    # print(sales.head())
    pivot_table_size = sales.pivot_table(index='purchase_month', columns='item_name', values='item_price', aggfunc='size', fill_value=0)
    print(pivot_table_size)
    print('#' * 10)
    pivot_table_sum = sales.pivot_table(index='purchase_month', columns='item_name', values='item_price', aggfunc='sum', fill_value=0)
    print(pivot_table_sum)
    print('#' * 10)

    # Fix data fluctuation
    print('unique length: {}'.format(len(sales['item_name'].unique())))
    sales['item_name'] = sales['item_name'].str.upper()
    sales['item_name'] = sales['item_name'].str.replace(' ', '')
    sales['item_name'] = sales['item_name'].str.replace('　', '')
    print('unique length: {}'.format(len(sales['item_name'].unique())))
    print(sales.sort_values(by='item_name', ascending=True))
    print(pd.unique(sales['item_name'].sort_values(ascending=True)))
    print('#' * 10)

    pivot_table_size = sales.pivot_table(index='purchase_month', columns='item_name', values='item_price',
                                         aggfunc='size', fill_value=0)
    pivot_table_sum = sales.pivot_table(index='purchase_month', columns='item_name', values='item_price',
                                         aggfunc='sum', fill_value=0)
    print(pivot_table_size)
    print('#' * 10)
    print(pivot_table_sum)
    print('#' * 10)

    # Fix lacked data
    print('#### check null ####')
    print(sales.isnull().any(axis=0))
    print('#### check na ####')
    print(sales.isna().any(axis=0))
    print('#' * 10)


