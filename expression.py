a,b,c=[int(input()) for i in 'abc']
print(max((a*b*c),a*(b+c),a+(b*c),(a+b)*c,a+b+c))
