import tkinter as tk
from tkinter import ttk
import sqlite3
import pyodbc

# Assuming the connection is established
conn_str = 'DSN=Control;UID='';PWD='''
connection = pyodbc.connect(conn_str)

if connection:
    print("We are connected")
else:
    print("Failed to connect")

sql = '''\
SELECT * FROM TAPR102_1.dbo.Table_1
'''
curser = connection.execute(sql)

root = tk.Tk()
root.title('SQL REPORT')

toolBar_frame = tk.Frame(root)
toolBar_frame.pack(side=tk.BOTTOM, fill=tk.X)

table = ttk.Treeview(root, columns=('Date Time', 'User', 'Operational Shift', 'Station Name', 'Process Name', 'Battery ID', 'Glue Weight', 'Cycle time'), show='headings')
# table = ttk.Treeview(root, columns=('Date Time', 'User', 'Operational Shift', 'Station Name', 'Process Name', 'Battery ID', 'Glue Weight', 'Cycle time'), show='headings')
# table = ttk.Treeview(parent=root, columns=('Sr.No', 'Date Time', 'User', 'Operational Shift', 'Station Name', 'Process Name', 'Battery ID', 'Glue Weight(grms)', 'Cycle time(sec)'), show='headings')

table.column('Date Time', width=100, minwidth=100, stretch=False)
table.column('User', width=100, minwidth=100, stretch=False)
table.column('Operational Shift', width=150, minwidth=100, stretch=False)
table.column('Station Name', width=150, minwidth=100, stretch=False)
table.column('Process Name', width=150, minwidth=100, stretch=False)
table.column('Battery ID', width=100, minwidth=100, stretch=False)
table.column('Glue Weight', width=150, minwidth=100, stretch=False)
table.column('Cycle time', width=150, minwidth=100, stretch=False)
table.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

i = 0
for ro in curser:
    table.insert('',i,text="",values=(ro[1],ro[2],ro[3],ro[4],ro[5],ro[6]))
    i = i + 1

exit_button = tk.Button(toolBar_frame, text='Exit', command=root.destroy)
exit_button.pack(side=tk.RIGHT)

root.mainloop()