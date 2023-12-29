import subprocess
import signal
import sys
import time


def signal_handler(sig, frame):
    print("Terminating processes...")
    process1.terminate()
    process2.terminate()
    sys.exit(1)

# Define the commands for each program
command1 = ["python", "SQL_Write.py"]
# command2 = ["python", "GUI_10.py"]

# Start the first process
process1 = subprocess.Popen(command1)

# Start the second process
process2 = subprocess.Popen(["pythonw", "GUI_8.py"], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)

# Set up a signal handler to catch termination signals
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
time.sleep(2)
try:
    # Wait for both processes to finish
    process1.wait()
    process2.wait()
except KeyboardInterrupt:
    # If Ctrl+C is pressed, terminate both processes
    signal_handler(signal.SIGINT, None)

print("Both programs have finished.")
