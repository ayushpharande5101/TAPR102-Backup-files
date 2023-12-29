import subprocess
import time

# Define the commands for each program
command1 = ["python", "SQL_Write.py"]
# command2 = ["pythonw", "GUI_9.py"]

# Start the first process
process1 = subprocess.Popen(command1)

# Start the second process
process2 = subprocess.Popen(["pythonw", "GUI_9.py"], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)

# Loop until the first process finishes
while process1.poll() is None:
    time.sleep(1)

# Close the second process if the first process is terminated
if process1.returncode is not None:
    process2.terminate()
    process2.wait()

print("Both programs have finished.")


