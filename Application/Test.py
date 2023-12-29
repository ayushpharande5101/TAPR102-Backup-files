import subprocess

# Define the commands for each program
command1 = ["python", "BACKEND_3_PLC.py"]
# command2 = ["python", "GUI_8.py"]

# Start the first process
process1 = subprocess.Popen(command1)

#process1 = subprocess.Popen(["pythonw", "SQL_Write.py"], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)

process2 = subprocess.Popen(["pythonw", "GUI_8.py"], shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)

# Start the second process
#process2 = subprocess.Popen(command2)

# Wait for both processes to finish
process1.wait()
process2.wait()

print("Both programs have finished.")

