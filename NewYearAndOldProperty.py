#https://codeforces.com/problemset/problem/611/B
def count(s1, n1, min1, max1):
    r = 0
    for i in xrange(s1 - 1, 0, -1):

        n1[i] = '0'
        if i < s1 - 1:
            n1[i + 1] = '1'

        val = int("".join(n1), 2)
        if val >= min1 and val <= max1:
            r += 1
        if val < y[0]: break
    return r

def update(l, ln):
    for i in xrange(ln):
        l[i] = '1'

y = map(int, raw_input().split())
n1 = list(bin(y[0])[2:])
n2 = list(bin(y[1])[2:])
s1 = len(n1)
s2 = len(n2)
r = 0

for i in xrange((s2 + 1) - s1):
    if(s1 + i > s1):
        n1.append('1')
    
    update(n1, s1 + i)

    r += count(s1 + i, n1, y[0], y[1])

print r