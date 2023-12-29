from tkinter import *
from tkinter import ttk
import tkinter as tk
from _datetime import datetime, date
import pandas as pd
import pyodbc
from PIL import ImageTk
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

logo_img = ImageTk.PhotoImage(file="C:/Users/Ayush Pharande/Downloads/CTPL2.png")
logo_w = tk.Label(view_bar_frame, image=logo_img)
logo_w.image = logo_img
logo_w.config(bg="#b0bed1")
logo_w.grid(row=0, column=0)

# After Entering any button.....Specific report would generate for as created before.

button1 = tk.Button(view_bar_frame, text="Foam Module")
button1.grid(row=0, column=1, padx=10, pady=10)
button1.config(relief=RAISED)
button2 = tk.Button(view_bar_frame, text="Gap Filler")
button2.grid(row=0, column=2, padx=10, pady=10)
button2.config(relief=RAISED)
button3 = tk.Button(view_bar_frame, text="Foam Encloser")
button3.grid(row=0, column=3, padx=10, pady=10)
button3.config(relief=RAISED)

# -------------------------------------------------------------
# add Checkbox

# ------------------------------------------------------------
view_report = tk.LabelFrame(view_bar_frame)
view_report.config(bg="#d5dfed", relief=FLAT, bd=5)
view_report.grid(row=0, column=4, padx=10, sticky="news")


def refresh_frames():
    # Clear table content
    for row in table.get_children():
        table.delete(row)

    # Clear date entries
    start_date_entry.delete(0, tk.END)
    end_date_entry.delete(0, tk.END)

    # Clear battery ID entry
    battery_id_entry.delete(0, tk.END)


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
        root.update_idletasks()

    elif var.get() == 2:  # Filtering by battery ID
        battery_id_val = battery_id_entry.get()

        sql = "SELECT * FROM TAPR102_1.dbo.Table_1 WHERE Battery_ID = ?"
        cursor = conn.execute(sql, (battery_id_val,))
        rows = cursor.fetchall()
        for row in rows:
            table.insert('', 'end', values=row)
        root.update_idletasks()

    else:
        sql = 'SELECT * FROM TAPR102_1.dbo.Table_1'
        cursor = conn.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            table.insert(parent='', index=tk.END, iid=None, text="", values=row)
        root.update_idletasks()


view_report_button = tk.Button(view_bar_frame, text="View Report", command=view)
view_report_button.config(relief=RAISED)
view_report_button.grid(row=0, column=9, padx=10, pady=10)
refresh_button = tk.Button(view_bar_frame, text='Refresh', command=refresh_frames)
refresh_button.grid(row=0, column=10, padx=10, pady=10)
# =====================================================================

toolBar_frame = tk.Frame(root, width=5000, height=1500)
toolBar_frame.config(bg="#b0bed1", relief=GROOVE, bd=5)
toolBar_frame.pack(fill=X, padx=10)

var = tk.IntVar()


def datetime():
    if var.get() == 1:
        start_date.grid(row=1, column=1)
        start_date_entry.grid(row=1, column=2)
        space.grid(row=1, column=3)

        end_date.grid(row=1, column=4)
        end_date_entry.grid(row=1, column=5)
        space1.grid(row=1, column=6)

        # remove the data of the previous radiobutton press
        battery_id.grid_forget()
        battery_id_entry.grid_forget()
        space2.grid_forget()


def Id():
    if var.get() == 2:
        battery_id.grid(row=1, column=7)
        battery_id_entry.grid(row=1, column=8, padx=3)
        space2.grid(row=1, column=9)

        # remove the data of the previous radiobutton press
        start_date.grid_forget()
        start_date_entry.grid_forget()
        space.grid_forget()

        end_date.grid_forget()
        end_date_entry.grid_forget()
        space1.grid_forget()


Option1 = tk.Radiobutton(toolBar_frame, text="By_Date", value=1, command=datetime)
Option2 = tk.Radiobutton(toolBar_frame, text="By_Id", value=2, command=Id)
Option1.grid(row=0, column=1, padx=5)
Option1.configure(variable=var)
Option2.grid(row=0, column=2, padx=5)
Option2.configure(variable=var)

start_date = tk.Label(toolBar_frame, text="Start-Date")
start_date.config(bg="#b0bed1")
start_date_entry = DateEntry(toolBar_frame, date_pattern='dd/mm/y')

end_date = tk.Label(toolBar_frame, text="End-Date")
end_date.config(bg="#b0bed1")
end_date_entry = DateEntry(toolBar_frame, date_pattern='dd/mm/y')

battery_id = tk.Label(toolBar_frame, text="Battery ID")
battery_id.config(bg="#b0bed1")
battery_id_entry = tk.Entry(toolBar_frame)

space = tk.Label(toolBar_frame, text="   ")
space.config(bg="#b0bed1")
space1 = tk.Label(toolBar_frame, text="   ")
space1.config(bg="#b0bed1")
space2 = tk.Label(toolBar_frame, text="   ")
space2.config(bg="#b0bed1")


# ---------------------------------------------------------------------------------------------------------------
def savefile():
    data = []
    for i in table.get_children():
        data.append([table.set(i, column) for column in table['columns']])

    df = pd.DataFrame(data,
                      columns=["Sr.No", "Date Time", "User", "Operational_Shift", "Station_Name", "Process_Name",
                               "Battery_ID", "Glue_Weight", "Cycle Time"])
    file_path = filedialog.asksaveasfilename(defaultextension='.xlsx',
                                             filetypes=[("Excel", ".xlsx"), ("Text File", ".txt"),
                                                        ("HTML file", ".html"),
                                                        ("All files", ".*")])
    df.to_excel(file_path, index=False)


button = tk.Button(toolBar_frame, text='Save', command=savefile)
button.grid(row=0, column=0, padx=10)

# ================================================================================================================


table_frame = tk.LabelFrame(root, width=5000, height=10000, text="Module Report", font=('Times New Roman', 20, 'bold'))
table_frame.config(relief=GROOVE, bd=5)
table_frame.pack(padx=10, fill=BOTH)

# table_name=tk.Label(table_frame, text="Module Report", font=('Times New Roman',20, 'bold'))
# table_name.pack()


# ---------------------------------------------------------------------------------------------------------

table = ttk.Treeview(table_frame, columns=(
    "Sr.No", "Date Time", "User", "Operational Shift", "Station Name", "Process Name",
    "Battery ID", "Glue Weight", "Cycle Time"), show="headings", height=1000)

# --------------------------------------------------------------------------------------------------
scrollbar_table = ttk.Scrollbar(table_frame, orient='horizontal', command=table.xview)
table.configure(xscrollcommand=scrollbar_table.set)
scrollbar_table.place(relx=0, rely=1, relwidth=1, anchor='sw')
# -------------------------------------------------------------------------------------------------

table.column("#0", width=0, stretch=tk.NO)
table.column("Sr.No", anchor=tk.CENTER, width=50)
table.column("Date Time", anchor=tk.CENTER, width=100)
table.column("User", anchor=tk.CENTER, width=100)
table.column("Operational Shift", anchor=tk.CENTER, width=100)
table.column("Station Name", anchor=tk.CENTER, width=100)
table.column("Process Name", anchor=tk.CENTER, width=100)
table.column("Battery ID", anchor=tk.CENTER, width=100)
table.column("Glue Weight", anchor=tk.CENTER, width=100)
table.column("Cycle Time", anchor=tk.CENTER, width=100)

table.heading("Sr.No", text="Sr.No")
table.heading("Date Time", text="Date Time")
table.heading("User", text="User")
table.heading("Operational Shift", text="Operational Shift")
table.heading("Station Name", text="Station Name")
table.heading("Process Name", text="Process Name")
table.heading("Battery ID", text="Battery ID")
table.heading("Glue Weight", text="Glue Weight")
table.heading("Cycle Time", text="Cycle Time")
table.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

i = 1
j = 1
for ro in curser:
    ro[-1] = int(ro[-1]) + j
    table.insert('', i, text="", values=(ro[-1], ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7]))
    print(ro[-1])
    j = j + 1
    i = i + 1

root.mainloop()