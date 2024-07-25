import time
from tkinter import *
import tkinter as tk
from tkinter import messagebox

# krijimi i tk window
root = Tk()

# madhesia
root.geometry("500x500")

#titulli
root.title("COUNTDOWN")
root["bg"] = "#40739e"

#lalbel tekste ne ballinen e faqes
label = tk.Label(root,text="COUNTDOWN" , font=("Times New Roman",20))
label.pack(padx=20, pady=20)
label.config(bg="#40739e", font=("Times New Roman",20, ""))

label = tk.Label(root,text="Use COUNTDOWN for more productive work time" , font=("Times New Roman",14))
label.pack(padx=10, pady=25)
label.config(bg="#40739e")
# variablat
hour = StringVar()
minute = StringVar()
second = StringVar()

# vendosja e valutes default ne 0
hour.set("0")
minute.set("00")
second.set("00")

def on_hover(event):
    event.widget.configure(bg="#ccd5ae")
def on_default(event):
    event.widget.configure(bg="#f5f6fa")
hourEntry = Entry(root, width=6, font=("Times New Roman", 18, ""), bd="0", justify="center",
               textvariable=hour)
hourEntry.place(x=215, y=180)
hourEntry.bind("<Enter>", on_hover)
hourEntry.bind("<Leave>", on_default)

def on_hover(event):
    event.widget.configure(bg="#ccd5ae")
def on_default(event):
    event.widget.configure(bg="#f5f6fa")
minuteEntry = Entry(root, width=6, font=("Times New Roman", 18, ""), bd="0", justify="center",
                    textvariable=minute)
minuteEntry.place(x=215, y=220)
minuteEntry.bind("<Enter>", on_hover)
minuteEntry.bind("<Leave>", on_default)

def on_hover(event):
    event.widget.configure(bg="#ccd5ae")
def on_default(event):
    event.widget.configure(bg="#f5f6fa")
secondEntry = Entry(root, width=6, font=("Times New Roman", 18, ""), bd="0", justify="center",
                    textvariable=second)
secondEntry.place(x=215, y=260)
secondEntry.bind("<Enter>", on_hover)
secondEntry.bind("<Leave>", on_default)
def submit():
    try:
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print("Please input the right value")
    while temp > -1:
        mins, secs = divmod(temp, 60)
        # Kthimi i input permes sekondave ne minuta dhe ore
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)


        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        root.update()
        time.sleep(1)

        # mesazhi kur vlera arrin 0
        if (temp == 0):
            messagebox.showinfo("COUNTDOWN", "Time's up, take a break ")
        temp -= 1


# button widget
def on_hover(event):
    event.widget.configure(bg="#ffa62b")
def on_default(event):
    event.widget.configure(bg="#f7f1e3")
btn = Button(root, text='Start COUNTDOWN Timer', bd='0', width=22, height=2, font=("Times New Roman", 10),
             command=submit)
btn.place(x=168, y=330)
btn.bind("<Enter>", on_hover)
btn.bind("<Leave>", on_default)

root.mainloop()