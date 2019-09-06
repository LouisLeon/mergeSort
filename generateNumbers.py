import os
import sys
import random

NUMBERS_TO_GENERATE = 1000

if len(sys.argv) < 2:
    print("Missed an argument. Defaulting to 1000.")
else:
    NUMBERS_TO_GENERATE = int(sys.argv[1])


with open("input.txt", "w") as file:
    for x in range(NUMBERS_TO_GENERATE):
        num = random.randint(1, 10001)
        file.write("%s " % num)
    print("SUCCESS")
