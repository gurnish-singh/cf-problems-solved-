g=input()
a='qwertyuiop'
b='asdfghjkl;'
c='zxcvbnm,./'
n=list(input())
if g=='R':
    for i in range (len(n)):
        if n[i] in a:
            n[i]=a[a.index(n[i])-1]
        elif n[i] in b:
            n[i]=b[b.index(n[i])-1] 
        else:
            n[i]=c[c.index(n[i])-1]
else:
    for i in range (len(n)):
        if n[i] in a:
            n[i]=a[a.index(n[i])+1]
        elif n[i] in b:
            n[i]=b[b.index(n[i])+1] 
        else:
            n[i]=c[c.index(n[i])+1]
print(''.join(n[0:]))
