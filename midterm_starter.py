import time
import random
import statistics

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

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
    Compare full scans on identical, unique inputs using median batch timings.
    """
    sizes = [250, 500, 1000, 2000, 4000]
    repeats = 7
    rng = random.Random(202)
    algorithms = [find_duplicates_slow, find_duplicates_fast]
    results = {algorithm: [] for algorithm in algorithms}

    def time_batch(algorithm, data, calls):
        start = time.perf_counter()
        for _ in range(calls):
            algorithm(data)
        return time.perf_counter() - start

    print("Median seconds per call (unique inputs, seven trials)")
    print(f"{'n':>6} {'Slow':>14} {'Fast':>14}")
    for n in sizes:
        data = list(range(n))
        rng.shuffle(data)
        batches = {}
        samples = {algorithm: [] for algorithm in algorithms}
        for algorithm in algorithms:
            assert algorithm(data) is False
            calls = 1
            while time_batch(algorithm, data, calls) < 0.02:
                calls *= 2
            batches[algorithm] = calls

        for trial in range(repeats):
            # Alternate order to reduce systematic first/second timing bias.
            order = algorithms if trial % 2 == 0 else algorithms[::-1]
            for algorithm in order:
                elapsed = time_batch(algorithm, data, batches[algorithm])
                samples[algorithm].append(elapsed / batches[algorithm])

        for algorithm in algorithms:
            results[algorithm].append(statistics.median(samples[algorithm]))
        print(f"{n:6d} {results[algorithms[0]][-1]:14.8f} "
              f"{results[algorithms[1]][-1]:14.8f}")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.loglog(sizes, results[find_duplicates_slow], "o-", label="Slow (O(n²))")
    ax.loglog(sizes, results[find_duplicates_fast], "o-", label="Fast (expected O(n))")
    ax.set_xlabel("Input size n (number of elements)")
    ax.set_ylabel("Median time per call (seconds)")
    ax.set_title("Duplicate detection: full scans on unique inputs")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend()
    fig.tight_layout()
    output = Path(__file__).resolve().with_name("results.png")
    fig.savefig(output, dpi=180)
    plt.close(fig)
    print(f"Saved plot to {output}")
    return results


if __name__ == "__main__":
    flawed_benchmark()
