import subprocess
import os
import signal

# Start SQL_Write.py
process1 = subprocess.Popen(["pythonw", "SQL_Write.py"], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)

# Start GUI_8.py
process2 = subprocess.Popen(["pythonw", "GUI_9.py"], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)

try:
    # Wait for both processes to finish
    process1.wait()
    process2.wait()

except KeyboardInterrupt:
    # Handle keyboard interrupt (Ctrl+C) to terminate both processes
    process1.terminate()
    process2.terminate()

    # Wait for processes to exit
    process1.wait()
    process2.wait()

print("Both programs have finished.")

