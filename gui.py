#GUI ->graphical user interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

#initialisasi window
window = tk.Tk()
window.configure(bg = "white")
window.geometry("500x500")
window.resizable(False, False)
window.title("Hello World")

#frame
frame = ttk.Frame(window)
#penempatan grid, pack, place
frame.pack(padx=20, pady=20, fill="x", expand=True)

#komponen - komponen
# 1. label untuk nama depan
label_first_name = ttk.Label(frame, text="First Name:")
label_first_name.pack(padx=20, pady=10, fill="x", expand=True)

# 2. entry untuk nama depan
first_name = tk.StringVar()
entry_first_name = ttk.Entry(frame,textvariable = first_name)
entry_first_name.pack(padx=20, pady=20, fill="x", expand=True)

# 3. label untuk nama belakang
label_second_name = ttk.Label(frame, text="Second Name:")
label_second_name.pack(padx=20, pady=10, fill="x", expand=True)

# 4. entry untuk nama belakang
second_name = tk.StringVar()
entry_second_name = ttk.Entry(frame,textvariable = second_name)
entry_second_name.pack(padx=20, pady=20, fill="x", expand=True)

# 5. tombol

greet_button = ttk.Button(frame, text="Hello...", command=lambda: print(f"Hello, {first_name.get()} {second_name.get()}! {showinfo(title='Greeting', message=f'Hello, {first_name.get()} {second_name.get()}!')}"))
greet_button.pack(padx=20, pady=20, fill="x", expand=True)



window.mainloop()
