def hloo(s,d,k):
    while(s<=d):
        yield s
        s=s+k
b=hloo(10,30,5)
print(next(b))
print(next(b))
