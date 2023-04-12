import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor

l = [3, 4, 5, 6, 7]


def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n


if __name__ == '__main__':
    started_at = time.time()
    executor = ProcessPoolExecutor(max_workers=5)
    results = executor.map(fac, l)
    for result in executor.map(fac, l):
        print(result)
    ppe_time = time.time() - started_at
    print(f'Time with ProcessPoolExecutor: {ppe_time} \n')

    started_at = time.time()
    executor = ThreadPoolExecutor(max_workers=5)
    results = executor.map(fac, l)
    for result in executor.map(fac, l):
        print(result)
    tpe_time = time.time() - started_at
    print(f'Time with ThreadPoolExecutor: {tpe_time} \n')

    if ppe_time > tpe_time:
        print("The best method is: ThreadPoolExecutor")
    else:
        print("The best method is: ProcessPoolExecutor")
