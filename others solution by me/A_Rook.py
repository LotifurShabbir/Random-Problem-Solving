# https://codeforces.com/contest/1907/problem/A
t = int(input())
a_side = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
num_side = ['1', '2', '3', '4', '5', '6', '7', '8']
for i in range(t):
    s = input()
    for row in a_side:
        for col in num_side:
            if (row == s[0] and col != s[1]) or (row != s[0] and col == s[1]):
                print(f'{row}{col}')