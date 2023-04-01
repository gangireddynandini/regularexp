def kvrrange(b,e):
    while(b<=e):
        yield b
        b=b+1
a=kvrrange(2,9)
while(True):
    try:
        print(next(a))
    except StopIteration:
        break