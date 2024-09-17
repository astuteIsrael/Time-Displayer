import tkinter as tk
from time import strftime

# To create a function to update the time
def time():
    current_time = strftime('%H:%M:%S %p')  # Get current time in Hour:Minute:Second format
    label.config(text=current_time)  # Update the label text
    label.after(1000, time)  # Update every 1000 milliseconds (1 second)

# To create the main window
root = tk.Tk()
root.title("Simple Time Displayer")

# To create a label widget to display the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')

label.pack(anchor='center')

# To start the time function to update the time
time()

# To run the application loop
root.mainloop()
