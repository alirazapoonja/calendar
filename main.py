import calendar
import tkinter as tk
from tkinter import scrolledtext

def show_calendar():
    year = 2025
    cal_text = calendar.TextCalendar().formatyear(year)
    text_area.delete('1.0', tk.END)  # Clear previous content
    text_area.insert(tk.INSERT, cal_text)

# Create main window
root = tk.Tk()
root.title("2025 Calendar")
root.geometry("600x500")

# Button to show calendar
show_button = tk.Button(root, text="Show Calendar", command=show_calendar, font=("Arial", 14))
show_button.pack(pady=10)

# Text area to display the calendar
text_area = scrolledtext.ScrolledText(root, width=80, height=25, font=("Courier", 10))
text_area.pack(pady=10)

# Run the application
root.mainloop()
