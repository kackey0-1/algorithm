"""
あなたは英語の文法チェック・修正システムの作成を担当しています。 このシステムを実現するには、英単語を複数形に変換する機能が必要です。
単語の複数形への変換は、次のルールに従い行われます。

入力された英単語を複数形に変換するプログラムを作成してください。
※必ずしも実在の英単語が入力されるわけではありません。単純に文字列を上記のルールに沿って変換するプログラムを作成してください。

# 入力例1
3
dog
cat
pig
# 出力例1
dogs
cats
pigs

# 入力例2
7
box
photo
axis
dish
church
leaf
knife
# 出力例2
boxes
photoes
axises
dishes
churches
leaves
knives

# 入力例3
2
study
play
# 出力例3
studies
plays
"""

"""
どのパターンに当てはまるか判定する関数
・末尾が s, sh, ch, o, x のいずれかである英単語の末尾に es を付ける
・末尾が f, fe のいずれかである英単語の末尾の f, fe を除き、末尾に ves を付ける
・末尾の1文字が y で、末尾から2文字目が a, i, u, e, o のいずれでもない英単語の末尾の y を除き、末尾に ies を付ける
・上のいずれの条件にも当てはまらない英単語の末尾には s を付ける
"""
def which(s):
    # pattern1: axis,dish,church,photo,box
    if s[-1] == 's' or s[-2]+s[-1] == 'sh' or s[-2]+s[-1] == 'ch' or s[-1] == 'o' or s[-1] == 'x':
        return s+'es'
    # pattern2: leaf
    elif s[-1] == 'f': 
        return s[:-1]+'ves'
    # pattern3: knife
    elif s[-2]+s[-1] == 'fe':
        return s[:-2]+'ves'
    # pattern4: study,play,pliy,pluy,pley,ploy
    elif s[-1] == 'y' and (s[-2] != 'a' and s[-2] != 'i' and s[-2] != 'u' and s[-2] != 'e' and s[-2] != 'o'):
        return s[:-1] +'ies'
    # pattern4: apple, banana
    else:
        return s+'s'

# pattern =  ["axis","dish","church","photo","box"]
# pattern = ["leaf"]
# pattern = ["knife"]
# pattern = ["study","play","pliy","pluy","pley","ploy"]
pattern = ["apple", "banana"]
for s in pattern:
    print(which(s))
