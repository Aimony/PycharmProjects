'''
六、图片旋转
图片旋转是对图片最简单的处理方式之一，在本题中，需要对图片顺时针旋转 90 度。用一个 n×m 的二维数组来表示一个图片，例如给出一个 3×4 的图片的例子：

1 3 5 7

9 8 7 6

3 5 9 7

这个图片顺时针旋转 90 度后的图片如下：

3 9 1

5 8 3

9 7 5

7 6 7

给定初始图片，请计算旋转后的图片。
【输入格式】

输入的第一行包含两个整数 n 和 m，分别表示行数和列数。接下来 n 行，每行 m 个整数，表示给定的图片。图片中的每个元素（像 素）为一个值为 0 至 255 之间的整数（包含 0 和 255）。

【输出格式】

输出 m 行 n 列，表示旋转后的图片。

解题思路
用数组来解决这道题。
分析题目，这道题的本质就是让数组图形进行90°的翻转，通过两个for循环就可以解决。
'''




n,m = map(int,input().split())
ls = []
for i in range(n):
    num = list(map(int,input().split()))
    ls.append(num)
new_ls = [[0] * n for i in range(m)]
for a in range(n):
    for b in range(m):
        new_ls[b][a] = ls[2 - a][b]

for i in range(len(new_ls)):
    for j in new_ls[i]:
        print(j,end='  ')
    print('')


















