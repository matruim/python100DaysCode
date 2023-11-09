import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

file_path = ""
watermark = Image.open('cyberpunk.png').convert('RGBA')


def adjust(image, size):
    image = image.resize((size[0], size[0] * image.size[1] // image.size[0]), resample=Image.Resampling.LANCZOS)
    new_image = Image.new('RGBA', size, (0, 0, 0, 0))
    new_image.paste(image, (0, (size[1] - image.size[1]) // 2))
    new_image.putalpha(50)
    return new_image


def open_image():
    global file_path
    file_path = filedialog.askopenfilename(title="Open Image File",
                                           filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])
    if file_path:
        display_image()


def get_watermarked_image():
    image_raw = Image.open(file_path).convert('RGBA')
    return Image.alpha_composite(image_raw, adjust(watermark, image_raw.size))


def save_image():
    full_path = os.path.dirname(file_path)
    get_watermarked_image().save(f'{full_path}/watermarked.png')


def display_image():
    photo = ImageTk.PhotoImage(get_watermarked_image())
    image_label.config(image=photo)
    image_label.photo = photo


root = tk.Tk()
root.title("Simple Image Viewer")

tk.Button(root, text="Open Image", command=open_image).pack(padx=20, pady=10)
image_label = tk.Label(root)
image_label.pack(padx=20, pady=20)
tk.Button(root, text="Save Image", command=save_image).pack(padx=20, pady=10)

root.mainloop()
