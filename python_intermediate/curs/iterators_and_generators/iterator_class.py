from math import sqrt


# Returns is a number is prime or not
def is_prime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False

    return True


# def get_n_primes(n):
#     primes = []
#     i = 2
#     while len(primes) != n:
#         if is_prime(i):
#             primes.append(i)
#         i += 1

#     return primes


# lst = get_n_primes(10000)
# for elem in lst:
#     print(elem)

class PrimeIterator:
    def __init__(self, n):
        self.n = n
        self.generated_numbers_count = 0
        self.number = 1

    def __iter__(self):
        return self

    # Functia "__next(self)__" ruleaza cand apelam "next()" pe iterator
    # intr-un obiect creat in afara clasei
    def __next__(self):
        self.number += 1

        if self.generated_numbers_count >= self.n:
            raise StopIteration
        elif is_prime(self.number):
            self.generated_numbers_count  += 1
            return self.number

        return self.__next__()


my_iter = PrimeIterator(100)
for elem in my_iter:
    print(elem)
