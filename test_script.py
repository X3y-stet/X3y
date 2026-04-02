import time
def slow_function():
    data = []
    for i in range(1000):
        data = data + [i] # This is slow in Python
    return data
