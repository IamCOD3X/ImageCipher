from PIL import Image
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

def insert_console_output(text):
    console_output.insert(tk.END, text + "\n")
    console_output.see(tk.END)

def encrypt_images(image_path, key):
    try:
        base_image = Image.open(image_path)
        img_array = np.array(base_image)

        np.random.seed(key)
        key_array = np.random.randint(0, 256, img_array.shape, dtype=np.uint8)

        encrypt_array = (img_array + key_array) % 256
        encrypt_image = Image.fromarray(encrypt_array)
        encrypt_image.save("encrypted_image.png")
        insert_console_output("Your Image has been encrypted and saved as 'encrypted_image.png'")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to encrypt image: {e}")

def decrypt_images(image_path, key):
    try:
        base_image = Image.open(image_path)
        img_array = np.array(base_image)

        np.random.seed(key)
        key_array = np.random.randint(0, 256, img_array.shape, dtype=np.uint8)

        decrypt_array = (img_array - key_array) % 256
        decrypt_image = Image.fromarray(decrypt_array)
        decrypt_image.save("decrypted_image.png")
        insert_console_output("Your Image has been decrypted and saved as 'decrypted_image.png'")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to decrypt image: {e}")

key = ()

