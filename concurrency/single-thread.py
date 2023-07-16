import time

import heavy


if __name__ == "__main__":
    start = time.time()
    heavy.sequential(20)
    end = time.time()
    print("BENCHMARK TIME: ", end - start)