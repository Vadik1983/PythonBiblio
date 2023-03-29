# Дано натуральное число n>1. Выведите все простые множители этого числа в 
# порядке неубывания с учетом кратности. Алгоритм должен иметь сложность O(logn).


n = 56


# def prime_factors(n, divisor=2):
#     if n == 1:
#         return
#     if n % divisor == 0:
#         print(divisor, end=" ")
#         prime_factors(n//divisor, divisor)
#     else:
#         prime_factors(n, divisor+1)

# prime_factors(n, divisor=2)

def wer(n):
    for i in range(2, n+1):
        if n%i == 0:
            if i == n:
                return [i]
            else:
                return [i] + wer(n//i)


print(wer(12))