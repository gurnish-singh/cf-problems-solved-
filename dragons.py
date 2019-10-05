s, n = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
a.sort(key = (lambda x: x[0]))
for i in range(n):
    if s <= a[i][0]:
        print('NO')
        break
    s += a[i][1]
else:
    print('YES')
