# GenAI Prep Day 1 follow-up practice
# Write code that:
# - imports contextmanager from contextlib
# - defines a context manager function named simple_timer
# - prints "Start" before yield
# - prints "End" after yield
# - uses with simple_timer():
# - prints "Working" inside the block

from contextlib import contextmanager
import time 

@contextmanager
def simple_timer():
    print("Start")
    start = time.time()
    yield
    end = time.time()
  
    print ("took " + str ( end - start )  + " seconds ")
    print("End")

with simple_timer():
    time.sleep(2)
    print("working")

