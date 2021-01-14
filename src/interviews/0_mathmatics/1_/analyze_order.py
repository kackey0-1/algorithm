import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':

    # 1. Load csv data
    customer = pd.read_csv('customer_master.csv')
    item = pd.read_csv('item_master.csv')
    transaction_1 = pd.read_csv('transaction_1.csv')
    transaction_detail_1 = pd.read_csv('transaction_detail_1.csv')

    print(customer.head())
    print('#'*100)
    print(transaction_1.head())
    print('#'*100)
    print(transaction_detail_1.head())
    print('#' * 100)
    # 2. Concatenate
    transaction_2 = pd.read_csv('transaction_2.csv')
    transaction = pd.concat([transaction_1, transaction_2], ignore_index=True)

    print(transaction.head())
    print(len(transaction), len(transaction_1), len(transaction_2))
    print('#' * 100)

    transaction_detail_2 = pd.read_csv('transaction_detail_2.csv')
    transaction_detail = pd.concat([transaction_detail_1, transaction_detail_2], ignore_index=True)
    print(transaction_detail.head())
    print(len(transaction_detail), len(transaction_detail_1), len(transaction_detail_2))
    print('#' * 100)

    # 3. Join
    join_data = pd.merge(transaction_detail, transaction[['transaction_id', 'payment_date', 'customer_id']],
                         on='transaction_id', how='left')
    print(join_data.head())
    print(len(transaction_detail), len(transaction), len(join_data))
    print('#' * 100)

    join_data = pd.merge(join_data, customer, on='customer_id', how='left')
    join_data = pd.merge(join_data, item, on='item_id', how='left')
    print(join_data.head())
    print('#' * 100)

    # 4. add new column column
    join_data['price'] = join_data['quantity'] * join_data['item_price']
    print(join_data[['quantity', 'item_price', 'price']].head())
    print('#' * 100)

    # 5. Sum price column
    print(join_data['price'].sum())
    print(transaction['price'].sum())
    print(transaction['price'].sum() == join_data['price'].sum())
    print('#' * 100)

    # 6. Show various statistics
    print(join_data.isnull().sum())
    print('#' * 100)
    print(join_data.describe())
    """
             detail_id     quantity          age     item_price          price
    count  7144.000000  7144.000000  7144.000000    7144.000000    7144.000000 # data volume
    mean   3571.500000     1.199888    50.265677  121698.628219  135937.150056 # average
    std    2062.439494     0.513647    17.190314   64571.311830   68511.453297 # 標準偏差
    min       0.000000     1.000000    20.000000   50000.000000   50000.000000 # 最小値
    25%    1785.750000     1.000000    36.000000   50000.000000   85000.000000
    50%    3571.500000     1.000000    50.000000  102500.000000  120000.000000
    75%    5357.250000     1.000000    65.000000  187500.000000  210000.000000 
    max    7143.000000     4.000000    80.000000  210000.000000  420000.000000 # 最大値
    """
    print(join_data.corr())
    print('#' * 100)

    # 7. data summary
    print(join_data.dtypes)
    print('#' * 100)
    join_data['payment_date'] = pd.to_datetime(join_data['payment_date'])
    join_data['payment_month'] = join_data['payment_date'].dt.strftime('%Y%m')
    print(join_data[['payment_date', 'payment_month']].head())
    print('#' * 100)
    print(join_data.groupby(['payment_month', 'item_name']).sum()[['price', 'quantity']])
    print('#' * 100)

    # 8. pivot table
    print(pd.pivot_table(join_data, index='item_name', columns='payment_month', values=['price', 'quantity'], aggfunc='sum'))
    print('#' * 100)

    # 9. show sales data by graph
    graph_data = pd.pivot_table(join_data, index='payment_month', columns='item_name', values='price', aggfunc='sum')
    print(graph_data.head())
    plt.plot(list(graph_data.index), graph_data["PC-A"], label="PC-A")
    plt.plot(list(graph_data.index), graph_data["PC-B"], label="PC-B")
    plt.plot(list(graph_data.index), graph_data["PC-C"], label="PC-C")
    plt.plot(list(graph_data.index), graph_data["PC-D"], label="PC-D")
    plt.plot(list(graph_data.index), graph_data["PC-E"], label="PC-E")
    plt.legend()
    plt.show()
    plt.close()
    print('#' * 100)














