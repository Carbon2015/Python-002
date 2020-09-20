import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, ** kwargs)
        end = time.time()
        print(f'run time is {end - start} ms')
        return result
    return wrapper

@timer
def test_timer():
    time.sleep(1)
    return

test_timer()