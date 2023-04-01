def kvrrange(b,e):
    while(b<=e):
        yield b
        b=b+1
a=kvrrange(2,9)
print(next(a))
print(next(a))
