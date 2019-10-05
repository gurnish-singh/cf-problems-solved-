n=[int (i) for i in range (1,(int(input())+1))]
l=[int(i) for i in input().split()]
k=[int(i) for i in input().split()]
count=0
for i in range (len(n)):
    if n[i] in l[1:] or n[i] in k[1:]:
        continue
    else:
        count=1

print(('I become the guy.','Oh, my keyboard!')[count==1])
