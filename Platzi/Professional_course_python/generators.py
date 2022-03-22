import time

def fibo_gen(max_num: int = None) -> int:
    """
    max_num: maximum value in the sequence.
    """
    n1, n2, counter = 0, 1, 0
    while (not max_num or n1 < max_num):
        # Option 2
        #if counter == 0:
        #    counter += 1
        #    yield n1
        #elif counter == 1:
        #    counter += 2
        #    yield n2
        #else:
        #    aux = n1 + n2
        #    n1, n2 = n2, aux
        #    counter += 1
        #    yield aux
        # Option 1
        yield n1
        n1, n2 = n2, n1 + n2
        counter += 1

if __name__ == "__main__":
    fibonacci = fibo_gen(5)
    for element in fibonacci:
        print(element)
        time.sleep(1)
        