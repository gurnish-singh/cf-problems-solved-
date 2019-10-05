a=input()
if (len(a)==1 and a.islower()):
    print(a.upper())
elif(a.isupper()):
    p=a.lower()
    print(p)
elif (a[1:].isupper()):
    p=a[0].upper()
    for i in range (1,len(a)):
        p+=(a[i].lower())
    print(p)
else:
    print(a)

    
