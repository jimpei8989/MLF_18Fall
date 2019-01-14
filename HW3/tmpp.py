def r(x):
    for i in range(x):
        yield i
a = r(10)
for i in a:
    print(i)

