python
import threading

shared_resource = 0
lock = threading.Lock()

def worker():
    global shared_resource
    for i in range(100000):
        with lock:
            shared_resource += 1

# Create two threads
thread1 = threading.Thread(target=worker)
thread2 = threading.Thread(target=worker)

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print(shared_resource)
In this example, two threads are created, each executing theworkerfunction. Theworkerfunction increments a shared resource 100,000 times. A lock is used to protect the shared resource and ensure that the increment operation is atomic.

Thread Pool

Python provides aconcurrent.futuresmodule that provides a high-level interface for parallelism. TheThreadPoolExecutorclass can be used to create a thread pool.

python
import concurrent.futures

def worker(name):
    print(f"Worker {name} started")
    for i in range(5):
        print(f"Worker {name}: {i}")
    print(f"Worker {name} finished")

# Create a thread pool with 2 threads
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    # Submit 2 tasks to the thread pool
    executor.submit(worker, "1")
    executor.submit(worker, "2")
In this example, a thread pool with 2 threads is created using theThreadPoolExecutorclass. Two tasks are submitted to the thread pool, each executing theworkerfunction.

Enter search terms...
