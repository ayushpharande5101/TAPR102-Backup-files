from tkinter import *
from tkinter import ttk
import tkinter as tk
from _datetime import datetime, date
import pandas as pd
import pyodbc
from tkcalendar import DateEntry
from tkinter import filedialog

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
root.geometry("800x685")
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
root.title(f"Material Handling- {current_time}")
root.icon = PhotoImage(file='C:/Users/Ayush Pharande/Downloads/CTPL2.png')
root.iconphoto(True, root.icon)
# root.config(bg='#586be8')

# ========================================================================
view_bar_frame = tk.Frame(root, width=5000, height=600)
view_bar_frame.pack(fill=X, padx=10, pady=10)
view_bar_frame.config(bg="#b0bed1", relief=RAISED, bd=5)
# -------------------------------------------------------------
# add Checkbox
var = tk.IntVar()

def datetime():
    if var.get() == 1:
        start_date.grid(row=1, column=0)
        start_date_entry.grid(row=1, column=1)
        space.grid(row=1, column=2)

        end_date.grid(row=1, column=3)
        end_date_entry.grid(row=1, column=4)
        space1.grid(row=1, column=5)

        # remove the data of the previous radiobutton press
        battery_id.grid_forget()
        battery_id_entry.grid_forget()
        space2.grid_forget()

def Id():
    if var.get() == 2:
        battery_id.grid(row=1, column=6)
        battery_id_entry.grid(row=1, column=7, padx=3)
        space2.grid(row=1, column=8)

        # remove the data of the previous radiobutton press
        start_date.grid_forget()
        start_date_entry.grid_forget()
        space.grid_forget()

        end_date.grid_forget()
        end_date_entry.grid_forget()
        space1.grid_forget()

Option1 = tk.Radiobutton(view_bar_frame, text="By_Date", value=1, command=datetime)
Option2 = tk.Radiobutton(view_bar_frame, text="By_Id", value=2, command=Id)
Option1.grid(row=0, column=0)
Option1.configure(variable=var)
Option2.grid(row=0, column=1, padx=10)
Option2.configure(variable=var)

start_date = tk.Label(view_bar_frame, text="Start-Date")
start_date.config(bg="#b0bed1")
start_date_entry = DateEntry(view_bar_frame, date_pattern='dd/mm/y')

end_date = tk.Label(view_bar_frame, text="End-Date")
end_date.config(bg="#b0bed1")
end_date_entry = DateEntry(view_bar_frame, date_pattern='dd/mm/y')

battery_id = tk.Label(view_bar_frame, text="Battery ID")
battery_id.config(bg="#b0bed1")
battery_id_entry = tk.Entry(view_bar_frame)

space = tk.Label(view_bar_frame, text="   ")
space.config(bg="#b0bed1")
space1 = tk.Label(view_bar_frame, text="   ")
space1.config(bg="#b0bed1")
space2 = tk.Label(view_bar_frame, text="   ")
space2.config(bg="#b0bed1")
# ------------------------------------------------------------
view_report = tk.LabelFrame(view_bar_frame)
view_report.config(bg="#d5dfed", relief=FLAT, bd=5)
view_report.grid(row=0, column=9, padx=10, sticky="news")

def view():
    conn_str = 'DSN=Control;UID='';PWD='''  # Your connection string here
    conn = pyodbc.connect(conn_str)

    if var.get() == 1:  # Filtering by date range
        start = start_date_entry.get_date().strftime('%Y-%m-%d')
        end = end_date_entry.get_date().strftime('%Y-%m-%d')

        sql = "SELECT * FROM TAPR102_1.dbo.Table_1 WHERE Date_Time_1 BETWEEN ? AND ?"
        cursor = conn.execute(sql, (start, end))
        rows = cursor.fetchall()
        for row in rows:
            table.insert('', 'end', values=row)

    elif var.get() == 2:  # Filtering by battery ID
        battery_id_val = battery_id_entry.get()

        sql = "SELECT * FROM TAPR102_1.dbo.Table_1 WHERE [Battery ID] = ?"
        cursor = conn.execute(sql, (battery_id_val,))
        rows = cursor.fetchall()
        for row in rows:
            table.insert('', 'end', values=row)
    else:
        sql = 'SELECT * FROM TAPR102_1.dbo.Table_1'
        cursor = conn.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            table.insert(parent='', index=tk.END, iid=None, text="", values=row)

view_report_button = tk.Button(view_report, text="View Report", command=view)
view_report_button.config(relief=RAISED)
view_report_button.grid(row=0, column=9, padx=10, pady=10)
# =====================================================================

toolBar_frame = tk.Frame(root, width=5000, height=40)
toolBar_frame.config(bg="#b0bed1", relief=GROOVE, bd=5)
toolBar_frame.pack(fill=X, padx=10)

# ---------------------------------------------------------------------------------------------------------------
def savefile():
    data = []
    for i in table.get_children():
        data.append([table.set(i, column) for column in table['columns']])

    df = pd.DataFrame(data,
                      columns=["Sr.No", "Date Time", "User", "Operational Shift", "Station Name", "Process Name", "Battery ID", "Glue Weight(grms)", "Cycle time(sec)"])
    file_path = filedialog.asksaveasfilename(defaultextension='.xlsx',
                                             filetypes=[("Excel", ".xlsx"), ("Text File", ".txt"),
                                                        ("HTML file", ".html"),
                                                        ("All files", ".*")])
    df.to_excel(file_path, index=False)

button = tk.Button(toolBar_frame, text='Save', command=savefile)
button.pack(side=LEFT)

# ================================================================================================================

table_frame = tk.LabelFrame(root, width=5000, height=5000, text="Module Report", font=('Times New Roman', 20, 'bold'))
table_frame.config(relief=GROOVE, bd=5)
table_frame.pack(padx=10, fill=BOTH)

# table_name=tk.Label(table_frame, text="Module Report", font=('Times New Roman',20, 'bold'))
# table_name.pack()

# ---------------------------------------------------------------------------------------------------------

table = ttk.Treeview(table_frame, columns=(
    "Sr.No", "Date Time", "User", "Operational Shift", "Station Name", "Process Name", "Battery ID",
    "Glue Weight(grms)",
    "Cycle time(sec)"), show="headings")

# --------------------------------------------------------------------------------------------------
scrollbar_table = ttk.Scrollbar(table_frame, orient='horizontal', command=table.xview)
table.configure(xscrollcommand=scrollbar_table.set)
scrollbar_table.place(relx=0, rely=1, relwidth=1, anchor='sw')
# -------------------------------------------------------------------------------------------------

table.column("#0", width=0, stretch=tk.NO)
table.column("Sr.No", anchor=tk.CENTER, width=100)
table.column("Date Time", anchor=tk.CENTER, width=100)
table.column("User", anchor=tk.CENTER, width=100)
table.column("Operational Shift", anchor=tk.CENTER, width=100)
table.column("Station Name", anchor=tk.CENTER, width=100)
table.column("Process Name", anchor=tk.CENTER, width=100)
table.column("Battery ID", anchor=tk.CENTER, width=100)
table.column("Glue Weight(grms)", anchor=tk.CENTER, width=100)
table.column("Cycle time(sec)", anchor=tk.CENTER, width=100)

table.heading("Sr.No", text="Sr.No")
table.heading("Date Time", text="Date Time")
table.heading("User", text="User")
table.heading("Operational Shift", text="Operational Shift")
table.heading("Station Name", text="Station Name")
table.heading("Process Name", text="Process Name")
table.heading("Battery ID", text="Battery ID")
table.heading("Glue Weight(grms)", text="Glue Weight")
table.heading("Cycle time(sec)", text="Cycle time")
table.column("Sr.No", width=50, minwidth=100, stretch=False)
table.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

i = 1
j = 1
for ro in curser:
    ro[-1] = int(ro[-1]) + j
    table.insert('', i, text="", values=(ro[-1], ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7]))
    print(ro[-1])
    j = j + 1
    i = i + 1

exit_button = tk.Button(toolBar_frame, text='Exit', command=root.destroy)
exit_button.pack(side=tk.RIGHT)
root.mainloop()