#https://codeforces.com/problemset/problem/567/A
t = int(raw_input())
c = map(int, raw_input().split())

s = []

for i in range(t):

    mx = max(abs(c[i] - c[0]), abs(c[i] - c[t - 1]))

    if i == 0:
        mn = abs(c[i] - c[i + 1])
    elif i == t - 1:
        mn = abs(c[i] - c[i - 1])
    else:
        mn = min(abs(c[i] - c[i - 1]), abs(c[i] - c[i + 1]))
    s.append([mn, mx])

for r in s:
    print r[0], r[1]