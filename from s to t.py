def isSubSequence(string1, string2, m, n): 
    # Base Cases 
    if m == 0:    return True
    if n == 0:    return False
  
    # If last characters of two strings are matching 
    if string1[m-1] == string2[n-1]: 
        return isSubSequence(string1, string2, m-1, n-1) 
  
    # If last characters are not matching 
    return isSubSequence(string1, string2, m, n-1) 
n=int(input())
for i in range (n):
    s=(input())
    m=len (s)
    t=(input())
    n=len(t)
    p=(input())
    d={}
    d2={}
    d3={}
    f=0
    if isSubSequence(s, t, m, n):
        for i in (s):
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in (t):
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1
        for i in (p):
            if i in d3:
                d3[i]+=1
            else:
                d3[i]=1
        for i in t:
            if i not in s and i not in p:
                f=1
                break
            elif i in s and i in p:
                if d2[i]<=d[i]+d3[i]:
                    continue
                else:
                    f=1
                    break
            elif i not in p:
                if d2[i]<=d[i]:
                    continue
                else:
                    f=1
                    break
            else:
                if d2[i]<=d3[i]:
                    continue
                else:
                    f=1
                    break
               
        print(('YES','NO')[f==1])
    else:
        print('NO')
    

        
    
