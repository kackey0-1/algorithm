# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
# 10 60
# 85 3
# 85 7
# 65 1
# 85 5
# 90 0
# 35 14
# 10 1
# 75 1
# 25 3
# 70 5

def score_check(score, absence, ok_line, id):
    grade = (score - (absence * 5))
    # print(score, absence, ok_line, id)
    if ok_line <= grade:
        print(id)


first = "10 20"
lines = ["85 3", "85 7", "65 1", "85 5", "90 0", "35 14", "10 1", "75 1", "25 3", "70 5"]
# line = input().split()
line = first.split()
loop, ok_line = int(line[0]), int(line[1])

for i in range(loop):
    # l = input().split()
    l = lines[i].split()
    score, absence = int(l[0]), int(l[1])
    score_check(score, absence, ok_line, i + 1)
