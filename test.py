import time, os, sys

for i in range(100):
    print(i)
    time.sleep(0.1)
    sys.stdout.write("\033[F")  # Cursor up one line
