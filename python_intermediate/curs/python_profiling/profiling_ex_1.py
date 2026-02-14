import threading
import multiprocessing
import timeit


def count(from_, to_):
    while from_ >= to_:
        from_ -= 1


def wo_threading_func():
    count(400000, 0)
    count(100000, 0)
    # print("Done! No threads.")


def with_threading_func():
    t1 = threading.Thread(target=count, args=(400000, 0))
    t2 = threading.Thread(target=count, args=(100000, 0))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # print("Done! With threads.")


def with_multiprocessing_func():
    p1 = multiprocessing.Process(target=count, args=(400000, 0))
    p2 = multiprocessing.Process(target=count, args=(400000, 0))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # print("Done! With multiprocessing.")


if __name__ == "__main__":
    # wo_threading_func()

    # with_threading_func()

    # with_multiprocessing_func()

    setup = """from __main__ import wo_threading_func, with_threading_func, with_multiprocessing_func"""

    t1 = timeit.timeit("wo_threading_func()", setup=setup, number=1)
    print(f"Fără threading: {t1:.5f}s")

    t2 = timeit.timeit("with_threading_func()", setup=setup, number=1)
    print(f"Cu threading: {t2:.5f}s")

    t3 = timeit.timeit("with_multiprocessing_func()", setup=setup, number=1)
    print(f"Cu multiprocessing: {t3:.5f}s")
