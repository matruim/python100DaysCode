import os
import subprocess
import threading
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Function to convert FLV to H.264
def convert_flv_to_h264(input_file, output_file, progress_var, file_label):
    command = ["ffmpeg", "-i", input_file, "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-c:a", "copy", output_file]
    subprocess.run(command)
    progress_var.set(100)
    file_label.config(text=f"Completed: {os.path.basename(input_file)}")

# Function to update progress bar value
def update_progress(progress_var, value):
    progress_var.set(value)

# Function to run file conversion in a separate thread
def run_file_conversion():
    total_files = 0
    completed_files = 0

    # Get list of FLV files in input folder
    flv_files = [file for file in os.listdir(input_folder) if file.endswith(".flv")]
    total_files = len(flv_files)

    # Update global progress bar for each file
    def update_progress_bar():
        nonlocal completed_files
        completed_files += 1
        progress_value = (completed_files / total_files) * 100
        global_progress_var.set(progress_value)
        if completed_files == total_files:
            convert_button.config(state="normal")

    # Run file conversion in a separate thread
    def convert_files():
        for file in flv_files:
            input_file = os.path.join(input_folder, file)
            output_file = os.path.join(output_folder, os.path.splitext(file)[0] + ".mp4")
            file_label.config(text=f"Converting: {os.path.basename(input_file)}")
            progress_var.set(0)
            convert_flv_to_h264(input_file, output_file, progress_var, file_label)
            window.after(100, update_progress_bar)

    convert_button.config(state="disabled")
    t = threading.Thread(target=convert_files)
    t.start()

# Create GUI window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open a file dialog to select the input folder
input_folder = filedialog.askdirectory(title="Select Input Folder")
if not input_folder:
    print("No input folder selected. Exiting...")
    sys.exit(1)

output_folder = os.path.join(input_folder, "output")

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Create GUI window
window = tk.Toplevel()
window.title("FLV to H.264 Converter")

# Create global progress bar
global_progress_var = tk.DoubleVar()
global_progress_bar = ttk.Progressbar(window, variable=global_progress_var, length=300, mode='determinate')
global_progress_bar.grid(row=0, column=0, padx=10, pady=10)

# Create label for current file
file_label = ttk.Label(window, text="", width=50, anchor='w')
file_label.grid(row=1, column=0, padx=10)

# Create progress bar for current file
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(window, variable=progress_var, length=300, mode='determinate')
progress_bar.grid(row=2, column=0, padx=10, pady=5)

# Create "Convert" button
convert_button = ttk.Button(window, text="Convert", command=run_file_conversion)
convert_button.grid(row=3, column=0, padx=10, pady=5)

# Start GUI event loop
window.mainloop()
