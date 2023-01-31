def primes1():
    primes = []
    for candidate in range(2, 100, 1):
        prime = True
        for other in range(2, 100, 1):
            if candidate % other == 0 and candidate != other:
                prime = False
        if prime:
            primes.append(candidate)
    print(primes)

def primes2():
    primes = [x for x in range(2, 100, 1)
              if all(x % y != 0 for y in range(2, 100, 1)
                     if x != y)]
    print(primes)

primes1()
primes2()

def square(x):
    return x**2

print(square(2))
print((lambda x: x**2)(2))

def power(y):
    return (lambda x: x**y)

print(power(2)(2))

# https://mybinder.org/v2/gh/eric-olsson-chalmers/TLE-python/HEAD