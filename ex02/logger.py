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
            if exec_time < 0.001:
                time_stamp = "0.000 ms"
            elif exec_time < 1:
                time_stamp =  f"{exec_time * 1000:.3f} ms"
            else:
                time_stamp =  f"{exec_time:.3f} s"
            return "[ exec-time = " + time_stamp + " ]"
        
        time_stamp = make_timestamp(end - start)
        mark = "cmaxime"
        with open(os.path.join(os.path.dirname(__file__), "machine.log"), "a") as f:
            f.write(f"({mark})Running: {func.__name__: <20} {time_stamp}\n")
    return wrapper

class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
    
    @log
    def boil_water(self):
        return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for i in range(0, 20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 10):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
