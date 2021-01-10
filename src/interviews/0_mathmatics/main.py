import matplotlib.pyplot as plt
from pylab import rcParams
import matplotlib
# import seaborn as sns

# データの扱いに必要なライブラリ
import pandas as pd
import numpy as np
import datetime as dt
import math

if __name__ == '__main__':
    # load data set
    df = pd.read_csv('data.csv')
    print(df.head())
    n = df['日平均気温']

    # 度数分布表描画
    rcParams['figure.figsize'] = 10, 10
    ax = df.plot(y=['日平均気温'], bins=10, alpha=0.5, figsize=(8, 4), kind='hist')

    # 出力
    plt.savefig('histgram.png')
    plt.close()


