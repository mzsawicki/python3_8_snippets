def fun(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


fun(10, 20, 30, d=40, e=50, f=60)       # Valid
fun(10, b=20, c=30, d=40, e=50, f=60)   # b cannot be a keyword argument
fun(10, 20, 30, 40, 50, f=60)           # e must be a keyword argument
