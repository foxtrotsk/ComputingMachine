import concurrent.futures
import time


start = time.perf_counter()


def do_something(sleep_time):
	
	""" A Sample Function with time delay to imitate an I/O bound function"""
	print(f"Sleeping for {sleep_time} second(s) ...")
	time.sleep(sleep_time)
	return f"Done sleeping for {sleep_time} seconds..."


with concurrent.futures.ThreadPoolExecutor() as executor:
	# f1 = executor.submit(do_something, 1.5)
	# f2 = executor.submit(do_something, 1.5)

	# print(f1.result())
	# print(f2.result())

	# ####################################################################################################
	#  Without threading this script will take 5 + 4 + 3 + 2 + 1 = 15 secs
	# With threading the script took 5 seconds
	results = [executor.submit(do_something, sec) for sec in range(5, 0, -1)]

	for res in concurrent.futures.as_completed(results):
		print(res.result())


finish = time.perf_counter()


print(f"Finished in {round(finish - start, 2)} second(s) ...")