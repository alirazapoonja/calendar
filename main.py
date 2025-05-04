import calendar
import tkinter as ti
from tkinter import scrolledtext

def show_calendar():
    year = 2025
    cal_text = calendar.TextCalendar().formatyear(year)
    text_area.delete('1.0', ti.END)  # Clear previous content
    text_area.insert(ti.INSERT, cal_text)

# Create main window
root = ti.Tk()
root.title("2025 Calendar")
root.geometry("600x500")

# Button to show calendar
show_button = ti.Button(root, text="Show Calendar", command=show_calendar, font=("Arial", 14))
show_button.pack(pady=10)

# Text area to display the calendar
text_area = scrolledtext.ScrolledText(root, width=80, height=25, font=("Courier", 10))
text_area.pack(pady=10)

# Run the application
root.mainloop()
