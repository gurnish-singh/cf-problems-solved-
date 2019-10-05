n = int(input())
a = list(map(int, input().split()))
x = max(a)
y = min(a)
cnt = 0
for i in range(n):
    if a[i] == x:
        cnt += i
        break
 
for i in range(n-1, -1, -1):
    if a[i] == y:
        if i < cnt: cnt -= 1
        cnt += n-1 - i
        break
 
print(cnt)
