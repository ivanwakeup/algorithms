'''
bucket sort
'''


# ---------------------------------------------------------------------------
# test data
# ---------------------------------------------------------------------------
import random

random.seed(42)

# classic bucket sort input: floats uniformly distributed in [0, 1)
FLOAT_CASES = [
    ("empty", []),
    ("single", [0.5]),
    ("two, reversed", [0.9, 0.1]),
    ("textbook (CLRS)", [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]),
    ("already sorted", [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]),
    ("reverse sorted", [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]),
    ("duplicates", [0.5, 0.1, 0.5, 0.3, 0.1, 0.5]),
    ("all identical", [0.42] * 8),
    # edge of the range: 0.0 should land in the first bucket, 0.999 must not index past the last
    ("range edges", [0.999, 0.0, 0.5, 0.0001, 0.9999]),
    # worst case: everything lands in one bucket, so the per-bucket sort does all the work
    ("clustered", [0.501, 0.503, 0.502, 0.509, 0.505, 0.507, 0.504]),
    ("random 20", [random.random() for _ in range(20)]),
    ("random 1000", [random.random() for _ in range(1000)]),
]

# general version: bucket sort over any numeric range (compute min/max to size buckets)
INT_CASES = [
    ("small ints", [29, 25, 3, 49, 9, 37, 21, 43]),
    ("with negatives", [-5, 3, -1, 0, 8, -10, 2]),
    ("wide range", [1, 1000000, 500, 2, 999999, 42]),
    ("all identical", [7, 7, 7, 7]),  # max == min: watch for divide by zero
    ("mixed floats", [3.5, -2.25, 0.0, 10.75, -2.25, 4.0]),
    ("random 500", [random.randint(-1000, 1000) for _ in range(500)]),
]


def run_tests(sort_fn, cases):
    for name, data in cases:
        expected = sorted(data)
        actual = sort_fn(list(data))
        status = "PASS" if actual == expected else "FAIL"
        print(f"{status}  {name}")
        if actual != expected:
            print(f"      input:    {data[:10]}{'...' if len(data) > 10 else ''}")
            print(f"      expected: {expected[:10]}")
            print(f"      got:      {actual[:10] if actual else actual}")


def selection_sort(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[j]<data[i]:
                data[i], data[j] = data[j], data[i]

def insertion_sort(data):
    #an array of size 1 is sorted, start on element 2
    for i in range(1, len(data)):
        key = data[i]
        prefix_begin = i - 1

        #starting from the right end of the prefix, swap the key with the element if its greater
        while prefix_begin>=0 and key < data[prefix_begin]:
            #this is the shifting larger elements to the right part
            data[prefix_begin+1], data[prefix_begin] = data[prefix_begin], data[prefix_begin+1]
            prefix_begin-=1


'''
use primarly for floats between 0 and 1
'''
def bucket_sort(data):

    def do_sort(data, type="insertion"):
        if type=="insertion":
            insertion_sort(data)
        elif type=="selection":
            selection_sort(data)
        else:
            raise TypeError("""invalid sort type specified!! use one of: ["insertion", "selection"]""")

    buckets = [[] for _ in range(len(data))]
    for item in data:
        bucket = int(item * len(data))
        buckets[bucket].append(item)

    result = []
    for buck in buckets:
        do_sort(buck)
        result.extend(buck)

    return result 

    



if __name__ == "__main__":
    run_tests(bucket_sort, FLOAT_CASES)
    # once your version handles arbitrary ranges:
    # run_tests(bucket_sort, INT_CASES)