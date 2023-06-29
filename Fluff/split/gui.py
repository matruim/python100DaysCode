import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import converter
import sys

# Function to exit the program
def exit_program():
    sys.exit(0)

# Create GUI window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open a file dialog to select the input folder
input_folder = filedialog.askdirectory(title="Select Input Folder")
if not input_folder:
    print("No input folder selected. Exiting...")
    sys.exit(1)

output_folder = os.path.join(input_folder, "Output")

# Create the Output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Create GUI window
window = tk.Toplevel()
window.title("FLV to H.264 Converter")

# Create label for current file
file_label = ttk.Label(window, text="", width=50, anchor='w')
file_label.grid(row=0, column=0, padx=10, pady=10)

# Create scrolling listbox for file status
file_listbox = tk.Listbox(window, width=50)
file_listbox.grid(row=1, column=0, padx=10, pady=5)

# Create "Convert" button
convert_button = ttk.Button(window, text="Start Conversion", command=lambda: converter.run_file_conversion(input_folder, output_folder, file_label, file_listbox, window))
convert_button.grid(row=2, column=0, padx=10, pady=5)

# Create "Exit" button
exit_button = ttk.Button(window, text="Exit", command=exit_program)
exit_button.grid(row=3, column=0, padx=10, pady=5)

# Assign global_convert_button and file_listbox to variables for access in converter.py
converter.global_convert_button = convert_button
converter.global_file_listbox = file_listbox

# Start GUI event loop
window.mainloop()
