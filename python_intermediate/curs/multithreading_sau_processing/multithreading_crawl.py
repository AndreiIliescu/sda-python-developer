import requests
import threading


def crawl(url, dest):
    try:
        result = requests.get(url).text
        with open(dest, "a") as f:
            f.write(result)
    except Exception:
        print("Some error!")


def no_threads(urls):
    for url in urls:
        crawl(url, "no_threads.txt")


def with_threads(urls):
    threads = []

    for url in urls:
        # create new thread for each URL
        th = threading.Thread(target=crawl, args=(url, "with_threads.txt"))
        th.start()
        threads.append(th)

    # waiting for all threads to finish
    for th in threads:
        th.join()


if __name__ == "__main__":
    urls = [
        "https://jsonplaceholder.typicode.com/comments/1",
        "https://jsonplaceholder.typicode.com/comments/2",
        "https://jsonplaceholder.typicode.com/comments/3",
        "https://jsonplaceholder.typicode.com/comments/4",
        "https://jsonplaceholder.typicode.com/comments/5",
        "https://jsonplaceholder.typicode.com/comments/6",
        "https://jsonplaceholder.typicode.com/comments/7",
        "https://jsonplaceholder.typicode.com/comments/8",
        "https://jsonplaceholder.typicode.com/comments/9",
        "https://jsonplaceholder.typicode.com/comments/10",
        "https://jsonplaceholder.typicode.com/comments/11",
    ]

    # no_threads(urls)
    with_threads(urls)

    print("Done!")
