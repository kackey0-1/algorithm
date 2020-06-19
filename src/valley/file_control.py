
"""
ファイル書き込み
"""
f = open('data/test.txt', 'w')
f.write("Test\n")
print("I am print", file=f)
print("I", "am", "hogehoge", sep='#', end='!', file=f)
f.close()
s = """\
AAA
BBB
CCC
DDD
"""

with open('data/text_with.txt', 'w') as f:
    f.write(s)
    # f.close()が不要

"""
ファイル読み込み
"""
with open('data/text_with.txt', 'r') as f:
    # print(f.read())
    while True:
        chunk = 2
        # 文字数ごとの読み込み
        line = f.read(chunk)
        # print(line)
        # 行ごとの読み込み
        # line = f.readline()
        # print(line, end='')
        if not line:
            break

"""
seek 処理
"""
with open('data/text_with.txt', 'r') as f:
    # print(f.tell())
    # print(f.read(1))
    # 何文字目に進みたいかを指定可能
    f.seek(5)
    # print(f.read(1))

with open('data/test.txt', 'r+') as f:
    # 書き込み読み込みで開く場合、r+を使うこと
    # w+をした場合、f.write()の時点でファイルの中身が消える
    f.write(s)
    f.seek(0)
    print(f.read())