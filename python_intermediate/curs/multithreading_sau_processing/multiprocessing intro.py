import threading
import multiprocessing


def count(from_, to_):
    while from_ >= to_:
        from_ -= 1


def wo_threading_func():
    count(400000, 0)
    count(100000, 0)
    print("Done! No threads.")

# GIL(Global Interpretor Lock)
# Codul de mai jos rula mai repede decat cel fara thread-uri
# Pentru ca Python nu ruleaza thread-urile cu adevarat in paralel
# doar ne ofera iluzia ca o face
def with_threading_func():
    t1 = threading.Thread(target=count, args=(400000, 0))
    t2 = threading.Thread(target=count, args=(100000, 0))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done! With threads.")


def with_multiprocessing_func():
    p1 = multiprocessing.Process(target=count, args=(400000, 0))
    p2 = multiprocessing.Process(target=count, args=(400000, 0))

    # starting the new processes
    p1.start()
    p2.start()

    # waiting for processes to finish
    p1.join()
    p2.join()

    print("Done! With multiprocessing.")

if __name__ == "__main__":
    wo_threading_func()

    with_threading_func()

    with_multiprocessing_func()
