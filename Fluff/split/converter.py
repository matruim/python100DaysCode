import os
import subprocess
import threading
import tkinter as tk

global_convert_button = None
global_file_listbox = None

def convert_flv_to_h264(input_file, output_file, file_label):
    command = ["ffmpeg", "-i", input_file, "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-c:a", "copy", output_file]
    subprocess.run(command)
    file_label.config(text=f"Completed: {os.path.basename(input_file)}")

def run_file_conversion(input_folder, output_folder, file_label, file_listbox, window):
    global global_convert_button, global_file_listbox
    total_files = 0
    completed_files = 0

    flv_files = [file for file in os.listdir(input_folder) if file.endswith(".flv") and not file.startswith("._")]
    total_files = len(flv_files)

    global_file_listbox.delete(0, tk.END)
    for file in flv_files:
        global_file_listbox.insert(tk.END, file)

    def convert_files():
        nonlocal completed_files
        threads = []
        max_threads = 3
        for i, file in enumerate(flv_files):
            input_file = os.path.join(input_folder, file)
            output_file = os.path.join(output_folder, os.path.splitext(file)[0] + ".mp4")
            file_label.config(text=f"Converting: {os.path.basename(input_file)}")
            global_file_listbox.itemconfig(i, {"bg": "yellow"})
            t = threading.Thread(target=convert_flv_to_h264, args=(input_file, output_file, file_label))
            t.start()
            threads.append(t)
            window.update()
            global_file_listbox.itemconfig(i, {"bg": "green"})
            completed_files += 1
            file_label.config(text=f"Completed: {os.path.basename(input_file)} ({completed_files}/{total_files})")
            window.update()

            if len(threads) >= max_threads:
                for thread in threads:
                    thread.join()
                threads = []

        for thread in threads:
            thread.join()

        global_convert_button.config(state="normal")
        global_file_listbox.delete(0, tk.END)

    global_convert_button.config(state="disabled")

    t = threading.Thread(target=convert_files)
    t.start()
