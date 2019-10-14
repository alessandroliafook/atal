#https://codeforces.com/problemset/problem/588/A
dias = int(raw_input())

value, custo = map(int, raw_input().split())
total = custo * value

for i in xrange(dias - 1):

    value, t_custo = map(int, raw_input().split())

    if t_custo < custo: custo = t_custo
    total += value * custo

print(total)    