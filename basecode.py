import tkinter as tk
import sqlite3
from tkinter import ttk, messagebox

con = sqlite3.connect("risk_index.db")
con.execute("CREATE TABLE IF NOT EXISTS risk(country TEXT, wri REAL, vul REAL, year INTEGER);")
con.execute("CREATE TABLE IF NOT EXISTS temperature(country TEXT, year INTEGER, temp REAL);")

def insert_data(country, wri, vul, year, temp):
    conn = sqlite3.connect("risk_index.db")
    conn.execute("INSERT INTO risk(country, wri, vul, year, temp) VALUES( '" + country + "', '" + wri +
                 "', '" + vul + "', '" + year + "', '" + temp + "' );")
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Data Saved Successfully.")


def insert():
    add_window = tk.Tk()
    add_window.title("Add Details")
    tk.Label(add_window).grid(row=0, column=0, columnspan=2)
    tk.Label(add_window, text="country:").grid(row=1, column=0)
    country_entry = tk.Entry(add_window, width=50)
    country_entry.grid(row=1, column=1, padx=25)
    tk.Label(add_window, text="wri:").grid(row=2, column=0)
    wri_entry = tk.Entry(add_window, width=50)
    wri_entry.grid(row=2, column=1, padx=25)
    tk.Label(add_window, text="vul:").grid(row=3, column=0)
    vul_entry = tk.Entry(add_window, width=50)
    vul_entry.grid(row=3, column=1, padx=25)
    tk.Label(add_window, text="year:").grid(row=4, column=0, padx=20)
    year_entry = tk.Entry(add_window, width=50)
    year_entry.grid(row=4, column=1, padx=25)
    tk.Label(add_window, text="temp:").grid(row=5, column=0)
    grade_entry = tk.Entry(add_window, width=50)
    grade_entry.grid(row=5, column=1, padx=25)

    tk.Button(add_window, text='Submit', activebackground='grey', activeforeground='white', command=lambda: submit()).grid(row=6, column=0, columnspan=2, pady=10)

    def submit():
        country = country_entry.get()
        wri = wri_entry.get()
        vul = vul_entry.get()
        year = str(year_entry.get())
        temp = str(grade_entry.get())
        insert_data(country, wri, vul, year, temp)
        add_window.destroy()

    add_window.mainloop()


def display():
    connn = sqlite3.connect("risk_index.db")
    display_window = tk.Tk()
    display_window.title("World Risk Index Database")
    table = ttk.Treeview(display_window)
    table["columns"] = ("one", "two", "three", "four", "five")

    table.heading("one", text="Country")
    table.heading("two", text="WRI")
    table.heading("three", text="Vulnerability")
    table.heading("four", text="Year")
    table.heading("five", text="Temperature Change")

    cursor = connn.execute("SELECT rowid,* FROM risk, temperature;")
    i = 0
    for row in cursor:
        table.insert('', i, text="Risk " + str(row[0]), values=(row[1], row[2], row[3], row[4], row[5]))
        i = i + 1
    table.pack()
    connn.close()


def update():
    update_window = tk.Tk()
    update_window.title("Update Details")
    tk.Label(update_window, text="Select the ID of country to be Updated:").grid(row=0, column=0, sticky="W", padx=10, columnspan=2)
    s_id = tk.Entry(update_window, width=50)
    s_id.grid(row=1, column=0, sticky="W", padx=10, columnspan=2)
    tk.Label(update_window, text="\nEnter the new values:").grid(row=2, column=0, sticky="W", padx=10, pady=10, columnspan=2)
    tk.Label(update_window, text="country:").grid(row=3, column=0, sticky="W", padx=10, pady=10)
    s_country = tk.Entry(update_window, width=50)
    s_country.grid(row=3, column=1, sticky="W", padx=10, pady=10)
    tk.Label(update_window, text="wri:").grid(row=4, column=0, sticky="W", padx=10, pady=10)
    s_wri = tk.Entry(update_window, width=50)
    s_wri.grid(row=4, column=1, sticky="W", padx=10, pady=10)
    tk.Label(update_window, text="vul:").grid(row=5, column=0, sticky="W", padx=10, pady=10)
    s_vul = tk.Entry(update_window, width=50)
    s_vul.grid(row=5, column=1, sticky="W", padx=10, pady=10)
    tk.Label(update_window, text="year No:").grid(row=6, column=0, sticky="W", padx=10, pady=10)
    s_year = tk.Entry(update_window, width=50)
    s_year.grid(row=6, column=1, sticky="W", padx=10, pady=10)
    tk.Label(update_window, text="temp").grid(row=7, column=0, sticky="W", padx=10, pady=10)
    s_temp = tk.Entry(update_window, width=50)
    s_temp.grid(row=7, column=1, sticky="W", padx=10, pady=10)
    tk.Button(update_window, text="Update", activebackground='grey', activeforeground='white',
              command=lambda: submit()).grid(row=8, column=0, padx=10, pady=10, columnspan=2)

    def submit():
        sid = s_id.get()
        scountry = s_country.get()
        swri = s_wri.get()
        svul = s_vul.get()
        syear = s_year.get()
        stemp = s_temp.get()
        scon = sqlite3.connect("risk_index.db")
        scon.execute("UPDATE risk SET country = '" + scountry + "',wri = '" + swri + "', vul = '" + svul +
                     "', year = '" + syear + "', temp = '" + stemp + "' WHERE rowid = " + sid + ";")
        scon.commit()
        scon.close()
        messagebox.showinfo("Success", "Data Updated Successfully.")
        update_window.destroy()
    update_window.mainloop()


def delete():
    delete_window = tk.Tk()
    delete_window.title("Delete Info ")
    tk.Label(delete_window, text="Enter country whose details are to be removed:").grid(row=0, column=0, padx=10, pady=10)
    d_country = tk.Entry(delete_window, width=50)
    d_country.grid(row=0, column=1, padx=10, pady=10)
    tk.Button(delete_window, text="Delete Details", activebackground='grey', activeforeground='white',
              command=lambda: submit()).grid(row=1, column=0, columnspan=2)
    tk.Label(delete_window).grid(row=2, column=0, columnspan=2)

    def submit():
        dcountry = d_country.get()
        dcon = sqlite3.connect("risk_index.db")
        dcon.execute("DELETE FROM risk, temperature WHERE country = '" + dcountry+"';")
        dcon.commit()
        dcon.execute("VACUUM;")
        dcon.commit()
        dcon.close()
        messagebox.showinfo("Success", "Deleted Successfully.")
        delete_window.destroy()
    delete_window.mainloop()


def search():
    search_window = tk.Tk()
    search_window.title("Search Risk Index Details")

    tk.Label(search_window, text="Enter the country whose details are to be searched:").grid(row=0, column=0,
                                                                                                     padx=10, pady=10)
    f_country = tk.Entry(search_window, width=50)
    f_country.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(search_window, text="Results:").grid(row=1, column=0, sticky="W", columnspan=2, padx=10, pady=10)

    tk.Button(search_window, text="Search", activebackground='grey', activeforeground='white',
              command=lambda: submit()).grid(row=2, column=0, columnspan=2)
    tk.Label(search_window).grid(row=3, column=0, sticky="W", columnspan=2, padx=10, pady=10)
    details = ttk.Treeview(search_window)
    details["columns"] = ("one", "two", "three", "four", "five")

    details.heading("one", text="country")
    details.heading("two", text="wri")
    details.heading("three", text="vul")
    details.heading("four", text="year No")
    details.heading("five", text="temp")

    def submit():
        for row in details.get_children():
            details.delete(row)

        fcountry = f_country.get()
        fcon = sqlite3.connect("risk_index.db")
        cursor = fcon.execute("SELECT rowid,* from risk, temperature WHERE country = '" + fcountry + "';")
        fcon.commit()

        i = 0
        for row in cursor:
            details.insert('', i, text="risk " + str(row[0]), values=(row[1], row[2], row[3], row[4], row[5]))
            i = i + 1

        details.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        fcon.close()
    search_window.mainloop()


con.close()
