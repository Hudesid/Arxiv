def tub_son(num):

    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def tub_generator():

    num = 2
    while True:
        if tub_son(num):
            yield num
        num += 1


prime_gen = tub_generator()


def tub_son_2():
    return next(prime_gen)


for i in range(1, 10):
    print(tub_son_2())