import matplotlib.pyplot as plt
from pylab import rcParams
import matplotlib
import seaborn as sns
import pandas as pd
import numpy as np
import datetime as dt
import math
import statistics
import random


def create_histgram(file_name: str) -> None:
    # load data set
    df = pd.read_csv(file_name)
    print(df.head())
    n = df['日平均気温']

    # 度数分布表描画
    rcParams['figure.figsize'] = 10, 10
    ax = df.plot(y=['日平均気温'], bins=20, alpha=0.5, figsize=(8, 4), kind='hist')

    # export
    # plt.savefig('histgram.png')
    plt.show()
    plt.close()


def create_scatter(file_name: str) -> None:
    df = pd.read_csv(file_name, header=0, index_col=0)
    n = df['kion'].count()
    # 箱ひげ図の設定
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    sns.boxplot(x='continent', y='kion', data=df, _showfliers=False, ax=ax)
    sns.stripplot(x='continent', y='kion', data=df, _jitter=True, color='black', ax=ax)
    plt.show()
    plt.close()


def pprint(name: str) -> None:
    print('##### {} #####'.format(name))


if __name__ == '__main__':

    # create_histgram('data.csv')
    # create_scatter('data.csv')
    l = [random.randint(0, 100) for _ in range(10)]
    print(l)
    # 1. 合計
    pprint('total')
    print(sum(l))
    # 2. 平均
    pprint('average')
    print(sum(l)/len(l))
    print(statistics.mean(l))

    # 3. 中央値:
    pprint('median')
    print(statistics.median(l))

    # 分散: 、データのばらつき具合を表す指標
    pprint('variance')
    print(statistics.variance(l))
    # 標準偏差: データのばらつきと平均を比較するには、以下の数式のとおり、分散の正の平方根で求める標準偏差を使用
    pprint('standard deviation')
    print(statistics.stdev(l))
    #
