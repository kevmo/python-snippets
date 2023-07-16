import time

def heavy(n, id_):
    for x in range(1, n):
        for y in range(1, n):
            x**y 
    
    print ("DONE: ", id_)


def sequential(n):
    for i in range(n):
        heavy(100, i)

if __name__ == "__main__":
    start = time.time()
    sequential(20)
    end = time.time()
    print("BENCHMARK TIME: ", end - start)