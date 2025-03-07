# Log File Tail Generator (Like tail -f in Linux)
#
# Problem Statement:
#
# Write a generator tail_file(file_path) that:
#
# Continuously monitors a log file for new lines and yields them as soon as they are written.
#
# Simulates tail -f in Linux, which is used for real-time log monitoring.
#
# The function should run indefinitely unless stopped.
#
# This is useful for real-time log monitoring in applications.

import time

def tail_file(file_path):

    with open(file_path,'r') as file:
        file.seek(0, 2)  # Move to the end of the file
        while True:
            line = file.readline()
            if line:
                yield line.strip()  # Yield new line without extra whitespace
            else:
                time.sleep(1)  # Wait for new lines to be added


log=tail_file("../Text.txt")
print(log.__next__())
