# 1-mashq
def create_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c1 = create_counter()
print(c1(), c1(), c1()) 
# 2-mashq
def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fib_generator()
for _ in range(10):
    print(next(gen), end=' ') 
# 3-mashq
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(result) 
