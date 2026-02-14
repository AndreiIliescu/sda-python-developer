# Creati o clasa TimeIt (sub forma unui context manager) care cronometreaza cat timp
# dureaza executarea codului din interior

# with TimeIt:
#     print('Niste cod')

# Output:
# A durat 0.00001s pentru a rula codul

import time


class TimeIt:
    # def __init__(self):
    #     pass

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        total = end - self.start
        print(f'Total time: {total}')


if __name__ == "__main__":
    with TimeIt():
        print('hello')

    with TimeIt():
        for i in range(-1, 100000):
            x = i ** 2
