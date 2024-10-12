# Romain Tranchant
# CIS 103: Lab 5
# Instructor:MD Ali
# Lab: Exploring Searching, Sorting, and Algorithm Efficiency
# Due on Oct 12, 2024, 11:59 PM

# Activity:
# Run the provided Python script (timing1.py) that prints the running times for problem sizes
# that double. Use the time library to measure and compare the runtime of an algorithm.
# After running the program, discuss:
# - How does the run time increase as the problem size doubles?
# - What patterns can you observe?
# - Which algorithmic complexities might this behavior represent?

import time

problemSize = 10000000
print("%12s%16s" % ("Problem Size", "Seconds"))
for count in range(5):
    start = time.time()
# The start of the algorithm
work = 1
for x in range(problemSize):
    work += 1
    work -= 1
# The end of the algorithm
elapsed = time.time() - start
print("%12d%16.3f" % (problemSize, elapsed))


problemSize = 20000000
print("%12s%16s" % ("Problem Size", "Seconds"))
for count in range(5):
    start = time.time()
# The start of the algorithm
work = 1
for x in range(problemSize):
    work += 1
    work -= 1
# The end of the algorithm
elapsed = time.time() - start
print("%12d%16.3f" % (problemSize, elapsed))


problemSize = 40000000
print("%12s%16s" % ("Problem Size", "Seconds"))
for count in range(5):
    start = time.time()
# The start of the algorithm
work = 1
for x in range(problemSize):
    work += 1
    work -= 1
# The end of the algorithm
elapsed = time.time() - start
print("%12d%16.3f" % (problemSize, elapsed))


problemSize = 80000000
print("%12s%16s" % ("Problem Size", "Seconds"))
for count in range(5):
    start = time.time()
# The start of the algorithm
work = 1
for x in range(problemSize):
    work += 1
    work -= 1
# The end of the algorithm
elapsed = time.time() - start
print("%12d%16.3f" % (problemSize, elapsed))
