def is_prime(number : int) -> bool:
    """
    Function to determine whether a number is a prime number
    :param number: The number to determine whether it is prime or not
    :return: Returns True if it is a prime number, False if it is not a prime number.
    """
    if number >= 2:
        for i in range(2, int(number**0.5) + 1):
#        while i * i <= number:
            if number % i == 0:
                return False
            # print(i, end=" ")
 #           i = i + 1
    else:
        return False
    return True

n1 = int(input())
n2 = int(input())

if n1 > n2:
    n1, n2 = n2, n1

for i in range(n1, n2+1):
    if is_prime(i):
        print(i, end=' ')

n = int(input())
if is_prime(n):
    print(f"{n}는(은) 소수입니다.")
else:
    print(f"{n}는(은) 소수가 아닙니다!")