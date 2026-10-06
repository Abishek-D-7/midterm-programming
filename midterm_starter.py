import time
import random

# =======================================================
# DO NOT MODIFY THE ALGORITHM IMPLEMENTATIONS
# =======================================================

def find_duplicates_slow(data):
    """An O(n^2) algorithm to find duplicates."""
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] == data[j]:
                return True
    return False

def find_duplicates_fast(data):
    """An O(n) algorithm to find duplicates."""
    seen = set()
    for item in data:
        if item in seen:
            return True
        seen.add(item)
    return False


# =======================================================
# YOUR TASK: FIX THE BENCHMARKING SCRIPT BELOW
# =======================================================

def flawed_benchmark():
    """
    This benchmarking function contains several methodological errors.
    Rewrite this function to properly and fairly compare the two algorithms to demonstrate their scaling behavior.
    """
    print("Running flawed benchmark...")
    
    n = 1000
    
    start_time = time.time()
    data1 = [random.randint(i, 10000) for i in range(n)]
    find_duplicates_slow(data1)
    end_time = time.time()
    print(f"Slow algorithm took: {end_time - start_time} seconds")
    
    start_time_2 = time.time()
    data2 = [random.randint(i, 10000) for i in range(n)]
    find_duplicates_fast(data2)
    end_time_2 = time.time()
    print(f"Fast algorithm took: {end_time_2 - start_time_2} seconds")


if __name__ == "__main__":
    flawed_benchmark()