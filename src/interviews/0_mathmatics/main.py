import matplotlib.pyplot as plt
from pylab import rcParams
import matplotlib
import seaborn as sns
import pandas as pd
from pandas import DataFrame
import numpy as np
import datetime as dt
import math
import statistics
import random


def create_histgram(data_frame: DataFrame) -> None:
    print(data_frame.head())
    n = data_frame['日平均気温']

    # 度数分布表描画
    rcParams['figure.figsize'] = 10, 10
    ax = data_frame.plot(y=['日平均気温'], bins=20, alpha=0.5, figsize=(8, 4), kind='hist')

    # export
    # plt.savefig('histgram.png')
    plt.show()
    plt.close()


def create_(data_frame: DataFrame) -> None:
    n = data_frame['kion'].count()
    # 箱ひげ図の設定
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    sns.boxplot(x='continent', y='kion', data=data_frame, _showfliers=False, ax=ax)
    sns.stripplot(x='continent', y='kion', data=data_frame, _jitter=True, color='black', ax=ax)
    plt.show()
    plt.close()


def create_scatter(data_frame: DataFrame) -> None:
    print(data_frame.head())
    n = data_frame['kion'].count()
    # データの変換
    plt.scatter(data_frame['ido'], data_frame['kion'], c="white", edgecolors='black')
    # x 軸、y 軸の設定
    plt.xlabel('TEMPERATURE')
    plt.ylabel('LATITUDE')
    # 散布図の出力
    plt.legend()
    plt.show()
    # plt.savefig('scatter.png')


def pprint(name: str) -> None:
    print('##### {} #####'.format(name))


if __name__ == '__main__':
    # データの読み込み
    data_frame = pd.read_csv('data/data.csv', header=0, index_col=0)
    values = []
    for value in data_frame['ido']:
        print(value)
        if value < 0:
            values.append(value * -1)
        values.append(value)
    df = pd.DataFrame(data=[[value] for value in values], columns=['ido'])
    data_frame['ido'] = df['ido']

    # create_histgram(data_frame)
    create_scatter(data_frame)

    pprint('相関係数')
    res = data_frame.corr()
    print(res)

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
