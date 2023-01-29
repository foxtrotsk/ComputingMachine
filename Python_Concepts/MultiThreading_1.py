import time
import threading


start = time.perf_counter()


# Create a function 

def do_something():
	
	""" A Sample Function with time delay to imitate an I/O bound function"""
	print("Sleeping for 1 second..")
	time.sleep(1)
	print("Done sleeping..")

# Call the function
# do_something()
# do_something()

# ####################################################################################################

# Create threads

# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# ####################################################################################################
# Create a for loop for multiple threads

thread_list = []

# Using thread.join() in the same loop will result in sequential execution. Create another loop 
for _ in range(10):
	t = threading.Thread(target=do_something)
	t.start()
	thread_list.append(t)

for thread in thread_list:
	thread.join()

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} second(s)..")

