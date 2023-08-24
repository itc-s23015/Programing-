import math


def gen_prime(x=2):
    """素数を返すジェネレータ関数（１）愚直な方法"""
    while True:
        for i in range(2, x):
            if x % i == 0:
                break
            else:
                yield x
                x += 1


def gen_prime1(x=2):
    """素数を返すジェネレータ関数（２）sqrt(x)以下だけ調べる方法"""
    while True:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                break
            else:
                yield x
                x += 1


i = gen_prime1()
for c in range(10):
    print(next(i), end="")
    print("")
