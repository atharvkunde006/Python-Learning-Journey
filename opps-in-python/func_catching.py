from functools import lru_cache
import time
@lru_cache(maxsize=None)
def my_function(x):
    time.sleep(5)
    return x * 5
print(my_function(20))
print("done for 20")
print(my_function(2))
print("done for 2")
print(my_function(6))
print("done for 6")
print(my_function(20))
print("done for 20")