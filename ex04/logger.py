import time
from random import randint
import os

#... your definition of log decorator...
def log(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        def make_timestamp(exec_time):
            if exec_time < 0.000:
                time_stamp = "0.000 ms"
            elif exec_time < 1:
                time_stamp =  f"{exec_time * 1000:.3f} ms"
            else:
                time_stamp =  f"{exec_time:.3f} s"
            time_stamp_prefix = "exec-time"
            return f"[ {time_stamp_prefix} = {time_stamp} ]"
        
        time_stamp = make_timestamp(end - start)
        mark = "cmaxime"
        with open(os.path.join(os.path.dirname(__file__), "machine.log"), "a") as f:
            f.write(f"({mark})Running: {func.__name__: <20} {time_stamp}\n")
    return wrapper