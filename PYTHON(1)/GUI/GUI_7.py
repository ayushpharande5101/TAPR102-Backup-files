from tkinter import *
from tkinter import ttk
import tkinter as tk
from _datetime import datetime, date
import pandas as pd
import pyodbc
from PIL import ImageTk
from tkcalendar import DateEntry
from tkinter import filedialog

# creating a Window
root = tk.Tk()
root.geometry("800x685")
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
root.title(f"Material Handling- {current_time}")
root.icon = PhotoImage(file='C:/Users/Ayush Pharande/Downloads/CTPL2.png')
root.iconphoto(True, root.icon)
# root.config(bg='#586be8')

# Creating a Frame on the root
view_bar_frame = tk.Frame(root, width=5000, height=600)
view_bar_frame.pack(fill=X, padx=10, pady=10)
view_bar_frame.config(bg="#b0bed1", relief=RAISED, bd=5)

# Display the image onto the view_bar_frame Frame
logo_img = ImageTk.PhotoImage(file="C:/Users/Ayush Pharande/Downloads/CTPL2.png")
logo_w = tk.Label(view_bar_frame, image=logo_img)
logo_w.image = logo_img
logo_w.config(bg="#b0bed1")
logo_w.pack(side=LEFT)

# ------------------------------------------------------------

#
generate = tk.Frame(view_bar_frame, width=500, height=600)
generate.pack(side=RIGHT, fill=Y)
generate.config(bg="#d5dfed")


def refresh_frames():
    # Clear table content
    for row in table.get_children():
        table.delete(row)

    # Clear date entries
    start_date_entry.delete(0, tk.END)
    end_date_entry.delete(0, tk.END)

    # Clear battery ID entry
    battery_id_entry.delete(0, tk.END)
    var.set(0)


def view():
    conn_str = 'DSN=Conrol;UID='';PWD='''  # Your connection string here
    conn = pyodbc.connect(conn_str)

    if var.get() == 1:  # Filtering by date range
        start = start_date_entry.get_date().strftime('%Y-%m-%d')
        end = end_date_entry.get_date().strftime('%Y-%m-%d')

        sql = "SELECT * FROM TAPR102_1.dbo.Table_1 WHERE DateTime BETWEEN ? AND ?"
        cursor = conn.execute(sql, (start, end))
        rows = cursor.fetchall()
        for row in rows:
            date_time = row[0].strftime('%Y-%m-%d %H:%M:%S')
            table.insert(parent='', index=tk.END, iid=None, values=[date_time] + list(row[1:]))
        root.update_idletasks()

    elif var.get() == 2:  # Filtering by battery ID
        battery_id_val = battery_id_entry.get()

        sql = "SELECT * FROM TAPR102_1.dbo.Table_1 WHERE [Battery ID] = ?"
        cursor = conn.execute(sql, battery_id_val)
        rows = cursor.fetchall()
        for row in rows:
            date_time = row[0].strftime('%Y-%m-%d %H:%M:%S')
            table.insert(parent='', index=tk.END, iid=None, values=[date_time] + list(row[1:]))
        root.update_idletasks()

    else:
        sql = 'SELECT * FROM TAPR102_1.dbo.Table_1'
        cursor = conn.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            date_time = row[0].strftime('%Y-%m-%d %H:%M:%S')
            table.insert(parent='', index=tk.END, iid=None, values=[date_time] + list(row[1:]))
        root.update_idletasks()


refresh_button = tk.Button(generate, text='Refresh', command=refresh_frames)
refresh_button.pack(side=tk.RIGHT, padx=5)
# =====================================================================

toolBar_frame = tk.Frame(root, width=5000, height=1500)
toolBar_frame.config(bg="#b0bed1", relief=GROOVE, bd=5)
toolBar_frame.pack(fill=X, padx=10)

view_report = tk.LabelFrame(toolBar_frame)
view_report.config(bg="#b0bed1", relief=FLAT, bd=5)
view_report.pack(fill=Y, side=LEFT)
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
        battery_id.grid(row=1, column=1)
        battery_id_entry.grid(row=1, column=2, padx=3)
        space2.grid(row=1, column=3)

        # remove the data of the previous radiobutton press
        start_date.grid_forget()
        start_date_entry.grid_forget()
        space.grid_forget()

        end_date.grid_forget()
        end_date_entry.grid_forget()
        space1.grid_forget()


def Foam_Module():
    conn_str = 'DSN=Control;UID='';PWD='''  # Your connection string here
    conn = pyodbc.connect(conn_str)

    if var.get() == 1:  # Filtering by date range
        start = start_date_entry.get_date().strftime('%Y-%m-%d')
        end = end_date_entry.get_date().strftime('%Y-%m-%d')
        sql = "SELECT * FROM TAPR102_1.dbo.Table_1 WHERE [Process Name]='Foam Module' AND DateTime BETWEEN ? AND ?"
        cursor = conn.execute(sql, (start, end))
        rows = cursor.fetchall()
        for row in rows:
            date_time = row[0].strftime('%Y-%m-%d %H:%M:%S')
            table.insert(parent='', index=tk.END, iid=None, values=[date_time] + list(row[1:]))
        root.update_idletasks()

    elif var.get() == 2:  # Filtering by battery ID
        battery_id_val = battery_id_entry.get()

        sql = "SELECT * FROM TAPR102_1.dbo.Table_1 WHERE [Process Name]='Foam Module' AND [Battery ID] = ?"
        cursor = conn.execute(sql, battery_id_val)
        rows = cursor.fetchall()
        for row in rows:
            date_time = row[0].strftime('%Y-%m-%d %H:%M:%S')
            table.insert(parent='', index=tk.END, iid=None, values=[date_time] + list(row[1:]))
        root.update_idletasks()

    else:
        sql = "SELECT * FROM TAPR102_1.dbo.Table_1 WHERE [Process Name]='Foam Module' "
        cursor = conn.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            date_time = row[0].strftime('%Y-%m-%d %H:%M:%S')
            table.insert(parent='', index=tk.END, iid=None, values=[date_time] + list(row[1:]))
        root.update_idletasks()


def Gap_Filling():
    conn_str = 'DSN=Control;UID='';PWD='''  # Your connection string here
    conn = pyodbc.connect(conn_str)

    if var.get() == 1:  # Filtering by date range
        start = start_date_entry.get_date().strftime('%Y-%m-%d')
        end = end_date_entry.get_date().strftime('%Y-%m-%d')

        sql = "SELECT * FROM TAPR102_1.dbo.Table_1 WHERE [Process Name]='Gap Filling' AND DateTime BETWEEN ? AND ?"
        cursor = conn.execute(sql, (start, end))
        rows = cursor.fetchall()
        for row in rows:
            date_time = row[0].strftime('%Y-%m-%d %H:%M:%S')
            table.insert(parent='', index=tk.END, iid=None, values=[date_time] + list(row[1:]))
        root.update_idletasks()

    elif var.get() == 2:  # Filtering by battery ID
        battery_id_val = battery_id_entry.get()

        sql = "SELECT * FROM TAPR102_1.dbo.Table_1 WHERE [Process Name]='Gap Filling' AND [Battery ID] = ?"
        cursor = conn.execute(sql, battery_id_val)
        rows = cursor.fetchall()
        for row in rows:
            date_time = row[0].strftime('%Y-%m-%d %H:%M:%S')
            table.insert(parent='', index=tk.END, iid=None, values=[date_time] + list(row[1:]))
        root.update_idletasks()

    else:
        sql = "SELECT * FROM TAPR102_1.dbo.Table_1 WHERE [Process Name]='Gap Filling'"
        cursor = conn.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            date_time = row[0].strftime('%Y-%m-%d %H:%M:%S')
            table.insert(parent='', index=tk.END, iid=None, values=[date_time] + list(row[1:]))
        root.update_idletasks()


def Foam_Encloser():
    conn_str = 'DSN=Control;UID='';PWD='''  # Your connection string here
    conn = pyodbc.connect(conn_str)

    if var.get() == 1:  # Filtering by date range
        start = start_date_entry.get_date().strftime('%Y-%m-%d')
        end = end_date_entry.get_date().strftime('%Y-%m-%d')

        sql = "SELECT * FROM TAPR102_1.dbo.Table_1 WHERE [Process Name]='Foam Encloser' AND DateTime BETWEEN ? AND ?"
        cursor = conn.execute(sql, (start, end))
        rows = cursor.fetchall()
        for row in rows:
            date_time = row[0].strftime('%Y-%m-%d %H:%M:%S')
            table.insert(parent='', index=tk.END, iid=None, values=[date_time] + list(row[1:]))
        root.update_idletasks()

    elif var.get() == 2:  # Filtering by battery ID
        battery_id_val = battery_id_entry.get()

        sql = "SELECT * FROM TAPR102_1.dbo.Table_1 WHERE [Process Name]='Foam Encloser' AND [Battery ID] = ?"
        cursor = conn.execute(sql, battery_id_val)
        rows = cursor.fetchall()
        for row in rows:
            date_time = row[0].strftime('%Y-%m-%d %H:%M:%S')
            table.insert(parent='', index=tk.END, iid=None, values=[date_time] + list(row[1:]))
        root.update_idletasks()

    else:
        sql = "SELECT * FROM TAPR102_1.dbo.Table_1 WHERE [Process Name]='Foam Encloser'"
        cursor = conn.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            date_time = row[0].strftime('%Y-%m-%d %H:%M:%S')
            table.insert(parent='', index=tk.END, iid=None, values=[date_time] + list(row[1:]))
        root.update_idletasks()


Var1 = IntVar()

button1 = tk.Radiobutton(view_report, text="Foam Module", value=1)
button1.grid(row=0, column=3, padx=10, pady=10)
button1.configure(variable=Var1)

button2 = tk.Radiobutton(view_report, text="Gap Filler", value=2)
button2.grid(row=0, column=4, padx=10, pady=10)
button2.configure(variable=Var1)

button3 = tk.Radiobutton(view_report, text="Foam Encloser", value=3)
button3.grid(row=0, column=5, padx=10, pady=10)
button3.configure(variable=Var1)

button4 = tk.Radiobutton(view_report, text="Combined", value=4)
button4.grid(row=0, column=6, padx=10, pady=10)
button4.configure(variable=Var1)
button4.select()


def view_button():
    if Var1.get() == 1:
        Foam_Module()
    elif Var1.get() == 2:
        Gap_Filling()
    elif Var1.get() == 3:
        Foam_Encloser()
    elif Var1.get() == 4:
        view()


view_report_button = tk.Button(generate, text="View Report", command=view_button)
view_report_button.config(relief=RAISED)
view_report_button.pack(side=tk.LEFT, padx=5)

Option1 = tk.Radiobutton(view_report, text="By_Date", value=1, command=datetime)
Option2 = tk.Radiobutton(view_report, text="By_Id", value=2, command=Id)
Option1.grid(row=0, column=0, padx=5)
Option1.configure(variable=var)
Option2.grid(row=0, column=1, padx=5)
Option2.configure(variable=var)

start_date = tk.Label(view_report, text="Start-Date")
start_date.config(bg="#b0bed1")
start_date_entry = DateEntry(view_report, date_pattern='dd/mm/y')

end_date = tk.Label(view_report, text="End-Date")
end_date.config(bg="#b0bed1")
end_date_entry = DateEntry(view_report, date_pattern='dd/mm/y')

battery_id = tk.Label(view_report, text="Battery ID")
battery_id.config(bg="#b0bed1")
battery_id_entry = tk.Entry(view_report)

space = tk.Label(view_report, text="   ")
space.config(bg="#b0bed1")
space1 = tk.Label(view_report, text="   ")
space1.config(bg="#b0bed1")
space2 = tk.Label(view_report, text="   ")
space2.config(bg="#b0bed1")

# ---------------------------------------------------------------------------------------------------------------
save_frame = tk.Frame(toolBar_frame)
save_frame.config(bg="#d5dfed", bd=5)
save_frame.pack(fill=Y, side=RIGHT)


def savefile():
    try:
        data = []
        for i in table.get_children():
            data.append([table.set(i, column) for column in table['columns']])

        df = pd.DataFrame(data,
                          columns=['DateTime', '[User]', '[Operational Shift]', '[Station Name]', '[Process Name]',
                                   '[Battery ID]', '[Glue Weight]', '[Cycle Weight]'])

        file_path = filedialog.asksaveasfilename(defaultextension='.xlsx',
                                                 filetypes=[("Excel", ".xlsx"), ("Text File", ".txt"),
                                                            ("HTML file", ".html"),
                                                            ("All files", ".*")])
        df.to_excel(file_path, index=False)

    except Exception as e:
        print(f'An error occurred: {e}')


button = tk.Button(save_frame, text='Save', command=savefile)
button.grid(row=0, column=7, padx=10, pady=10)

# ================================================================================================================

table_frame = tk.LabelFrame(root, width=5000, height=5000, text="Module Report", font=('Times New Roman', 20, 'bold'))
table_frame.config(relief=GROOVE, bd=5)
table_frame.pack(padx=10, fill=BOTH)

# table_name=tk.Label(table_frame, text="Module Report", font=('Times New Roman',20, 'bold'))
# table_name.pack()

# ---------------------------------------------------------------------------------------------------------

table = ttk.Treeview(table_frame, columns=(
    'DateTime', '[User]', '[Operational Shift]', '[Station Name]', '[Process Name]', '[Battery ID]', '[Glue Weight]',
    '[Cycle Weight]'), show="headings", height=1000)

# --------------------------------------------------------------------------------------------------
scrollbar_table = ttk.Scrollbar(table_frame, orient='horizontal', command=table.xview)
table.configure(xscrollcommand=scrollbar_table.set)
scrollbar_table.place(relx=0, rely=1, relwidth=1, anchor='sw')
# -------------------------------------------------------------------------------------------------

table.column("#0", width=0, stretch=tk.NO)
# table.column("Sr.No", anchor=tk.CENTER, width=50)
table.column("DateTime", anchor=tk.CENTER, width=100)
table.column("[User]", anchor=tk.CENTER, width=100)
table.column("[Operational Shift]", anchor=tk.CENTER)
table.column("[Station Name]", anchor=tk.CENTER, width=100)
table.column("[Process Name]", anchor=tk.CENTER, width=100)
table.column("[Battery ID]", anchor=tk.CENTER)
table.column("[Glue Weight]", anchor=tk.CENTER)
table.column("[Cycle Weight]", anchor=tk.CENTER)

# table.heading("Sr.No", text="Sr.No")
table.heading("DateTime", text="DateTime")
table.heading("[User]", text="[User]")
table.heading("[Operational Shift]", text="[Operational Shift]")
table.heading("[Station Name]", text="[Station Name]")
table.heading("[Process Name]", text="[Process Name]")
table.heading("[Battery ID]", text="[Battery ID]")
table.heading("[Glue Weight]", text="[Glue Weight]")
table.heading("[Cycle Weight]", text="[Cycle Weight]")
table.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()