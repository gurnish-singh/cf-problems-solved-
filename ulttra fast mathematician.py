a,b=(input() for i in 'ab')
c=[0]*len(a)
for i in range (len(a)):
    if a[i]==b[i]:
        print('0',end='')
    else:
        print('1',end='')

