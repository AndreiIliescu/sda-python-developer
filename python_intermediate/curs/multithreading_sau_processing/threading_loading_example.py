import threading
import time


def long_task():
    print("Starting task ...")
    time.sleep(5) # simulam un task mai lung
    print("End task.")


task_thread = threading.Thread(target=long_task)

def show_progress():
    while task_thread.is_alive():
        print("Loading .....")
        time.sleep(1) # afisam mesajul de loading odata la o secunda


progress_thread = threading.Thread(target=show_progress)

task_thread.start()
progress_thread.start()

task_thread.join()
progress_thread.join()
