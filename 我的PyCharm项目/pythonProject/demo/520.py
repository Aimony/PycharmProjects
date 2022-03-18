LINES1 = """
000 111 222
0     1 2 2
000 111 2 2
  0 1   2 2
000 111 222
"""


def happy520(words, lines, num=3):
    for i in range(num):
        lines = lines.replace(str(i), words[i])

    lines = lines.replace(" ", chr(12288))
    print(lines)


words1 = "祝脱单"
happy520(words1, LINES1)

words1 = "我爱你"
happy520(words1, LINES1)

words1 = "爱永恒"
happy520(words1, LINES1)


print('------------------------------------------------------------')
LINES2 = """
000 111 222  3  444  5  6 6
0     1 2 2  3    4  5  6 6
000 111 2 2  3  444  5  666
  0 1   2 2  3    4  5    6
000 111 222  3  444  5    6
"""

words1 = "有情人终成眷属"
happy520(words1, LINES2, 7)
two = ["两情若是久长时", "金风玉露永相随"]
for w in two:
    happy520(w, LINES2, 7)