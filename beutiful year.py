t=int(input())
while(True):
    t+=1
    c=set(str(t))
    if len(c)==len(str(t)):
        print(t)
        break
