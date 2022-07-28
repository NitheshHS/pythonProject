import time
import random

# print(time.time())
# print(time.localtime())
# print(time.gmtime())

wait = random.randint(0,6)
input("press enter to start")
start_time = time.time()
time.sleep(wait)
print(start_time)
input("enter enter to stop")
end_time = time.time()

print(f"difference: {end_time - start_time}")