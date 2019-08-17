num = int(input())
is_prime(num)


def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            print(num, 'is not prime')
            break
    else:  # If never mod zero, then prime
        print(num, 'is prime!')
