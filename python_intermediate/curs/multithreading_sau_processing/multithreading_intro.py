import threading


def iterate_message(msg):
    for i in msg:
        print(i)


if __name__ == "__main__":
    # creating threads
    t1 = threading.Thread(target=iterate_message, args=("HelloWorldHelloPython!",))
    t2 = threading.Thread(target=iterate_message, args=("1234567890987654321",))

    # starting threads
    t1.start()
    t2.start()

    # waiting for threads to finish execution before continuing
    t1.join()
    t2.join()

    print("Done!")
