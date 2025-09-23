import time

def start_timer(task):
    print(f"Starting {task}...")
    start = time.time()
    input("Press Enter to stop ")
    end = time.time()
    duration = (end - start) / 60
    print(f"{task} done: {duration:.2f} minutes")
    return duration

if __name__ == "__main__":
    start_timer("Python")

