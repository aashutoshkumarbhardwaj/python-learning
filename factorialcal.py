import math
import multiprocessing
import time
import sys
import time


sys.set_int_max_str_digits(1000000)

def compute_factorial(n):
    print(f"Computing factorial of {n}")
    result = math.factorial(n)
    print(f"Factorial of {n} is {result}")

if __name__ == '__main__':
    numbers= [10000, 20000, 30000, 40000]  # Large numbers for factorial computation
    
    start_time = time.time()


    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(compute_factorial, numbers)
    end_time = time.time()

    