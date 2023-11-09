import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


file_path = ""
watermark = Image.open('cyberpunk.png')


def adjust(image, size):
    image = image.convert('RGBA')
    width, height = image.size
    new_width = size[0]
    new_height = new_width * height // width
    image = image.resize((new_width, new_height), resample=Image.Resampling.LANCZOS)
    new_image = Image.new('RGBA', size, (0, 0, 0, 0))
    upper = (size[1] - image.size[1]) // 2
    new_image.paste(image, (0, upper))
    new_image.putalpha(50)
    return new_image


def open_image():
    global file_path
    file_path = filedialog.askopenfilename(title="Open Image File",
                                           filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico")])
    if file_path:
        display_image()

def get_watermarkedImage():
    global watermark
    image_raw = Image.open(file_path).convert('RGBA')
    watermark = adjust(watermark, image_raw.size)
    return Image.alpha_composite(image_raw, watermark)


def save_image():
    fullpath = os.path.dirname(file_path)
    print(f'{fullpath}/watermarked.png')
    image = get_watermarkedImage()
    image.save(f'{fullpath}/watermarked.png')


def display_image():
    photo = ImageTk.PhotoImage(get_watermarkedImage())
    image_label.config(image=photo)
    image_label.photo = photo


root = tk.Tk()
root.title("Simple Image Viewer")
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(padx=20, pady=10)
image_label = tk.Label(root)
image_label.pack(padx=20, pady=20)
save_button = tk.Button(root, text="Save Image", command=save_image)
save_button.pack(padx=20, pady=10)
root.mainloop()
