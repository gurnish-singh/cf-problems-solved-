count=0
g=0
for i in (input()):
    if i=='4' or i=='7':
        count+=1
c=str(count)
for i in c:
    if i=='4' or i=='7':
        continue
    else:
        g=1
        break
print(('YES','NO')[g==1])
