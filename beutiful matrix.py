for i in range (5):
    s=input()[::2]
    if '1' in s:
        print(abs(i-2)+abs(s.index('1')-2))
