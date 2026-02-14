import datetime
import functools
import threading
import time


def execute_only_at_night_time(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        now = datetime.datetime.now().time()
        start = datetime.time(23, 0)
        end = datetime.time(6, 0)

        if (now >= start) or (now <= end):
            return func(*args, **kwargs)
        else:
            print(f"/=== This operation can only be performed between 23:00 and 06:00. Current time: {now} ===/\n")
            return None

    return wrapper


def loading(total_seconds=5):

    def decorator(func):

        def wrapper(*args, **kwargs):

            def run():
                start_time = time.time()
                dots = 0
                while time.time() - start_time < total_seconds:
                    dots = (dots % 3) + 1
                    print("\rLoading" + " ." * dots, end="")
                    time.sleep(0.5)
                print("\rLoading... Done!\n")
                func(*args, **kwargs)

            thread = threading.Thread(target=run)

            thread.start()
            thread.join()

        return wrapper

    return decorator
