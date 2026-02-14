# Implementati iteratorul CountDown

class CountDown:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        current = self.n
        self.n -= 1
        return current


c = CountDown(4)
print(next(c))
print(next(c))
print(next(c))
print(next(c))

# Output:
# 4
# 3
# 2
# 1
