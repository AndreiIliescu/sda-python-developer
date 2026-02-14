# Creati o clasa TimeIt (sub forma unui context manager) care cronometreaza cat timp
# dureaza executarea codului din interior

# with TimeIt:
#     print("Niste cod")


# Output
# A durat 0.00001s pentru a rula codul


import time


class TimeIt:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"A durat {time.time() - self.start:.5f}s pentru a rula codul")


with TimeIt():
    for timer in range(0, 1000000):
        pass
