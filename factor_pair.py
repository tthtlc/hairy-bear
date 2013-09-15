
def f(value):
    factors = []
    for i in range(1, int(value**0.5)+1):
        if value % i == 0:
            factors.append((i, value / i))
    return factors

print f(632382)
