import random
import time
import sys

sys.setrecursionlimit(20000)

comparisons = 0


# ---------- Partition Function ----------
def partition(arr, low, high):
    global comparisons

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        comparisons += 1

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# ---------- Deterministic Quick Sort ----------
def deterministic_quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)


# ---------- Randomized Quick Sort ----------
def randomized_quicksort(arr, low, high):
    if low < high:

        # Choose a random pivot
        rand_index = random.randint(low, high)
        arr[rand_index], arr[high] = arr[high], arr[rand_index]

        pi = partition(arr, low, high)

        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)


# ---------- Performance Test ----------
def run_test(sort_function, arr):
    global comparisons

    a = arr[:]
    comparisons = 0

    start = time.perf_counter()

    sort_function(a, 0, len(a) - 1)

    elapsed = (time.perf_counter() - start) * 1000

    return comparisons, elapsed


# ---------- Test Cases ----------
N = 5000

test_cases = {
    "Random": [random.randint(1, 100000) for _ in range(N)],
    "Sorted": list(range(N)),
    "Reverse": list(range(N, 0, -1)),
    "Nearly Sorted": list(range(N))
}

# Slightly shuffle Nearly Sorted array
ns = test_cases["Nearly Sorted"]

for _ in range(N // 20):
    i = random.randint(0, N - 1)
    j = random.randint(0, N - 1)
    ns[i], ns[j] = ns[j], ns[i]


# ---------- Output ----------
print(f"{'Input Type':<16} {'DQS Comps':>12} {'DQS Time(ms)':>15} {'RQS Comps':>12} {'RQS Time(ms)':>15}")
print("-" * 75)

for case, arr in test_cases.items():
    d_comp, d_time = run_test(deterministic_quicksort, arr)
    r_comp, r_time = run_test(randomized_quicksort, arr)

    print(f"{case:<16} {d_comp:>12} {d_time:>15.2f} {r_comp:>12} {r_time:>15.2f}")