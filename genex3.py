def kvrrange(b,e,s):
    while(b>=e):
        yield b
        b=b+s
k=kvrrange(100,20,-2)
while(True):
    try:
        print(next(k))
    except StopIteration:
        break

