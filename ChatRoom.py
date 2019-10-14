#https://codeforces.com/problemset/problem/58/A

entry = raw_input()

cont = 0
find = False

for l in entry:
    if cont == 0 and l == "h":
        cont += 1
    if cont == 1 and l == "e":
        cont += 1
    if (cont == 2 or cont == 3) and l == "l":
        cont += 1
    if cont == 4 and l == "o":
        find = True
        break

if find:
    print("YES")
else:
    print("NO") 