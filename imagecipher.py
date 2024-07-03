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

def browse_image():
    filename = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")])
    if filename:
        image_path_entry.delete(0, tk.END)
        image_path_entry.insert(0, filename)

def on_encrypt():
    image_path = image_path_entry.get()
    key = key_entry.get()
    if not image_path or not key:
        messagebox.showwarning("Input Error", "Please provide both the image path and the key.")
        return
    try:
        key = int(key)
        encrypt_images(image_path, key)
    except ValueError:
        messagebox.showwarning("Input Error", "Key must be an integer.")

def on_decrypt():
    image_path = image_path_entry.get()
    key = key_entry.get()
    if not image_path or not key:
        messagebox.showwarning("Input Error", "Please provide both the image path and the key.")
        return
    try:
        key = int(key)
        decrypt_images(image_path, key)
    except ValueError:
        messagebox.showwarning("Input Error", "Key must be an integer.")

root = tk.Tk()
root.title("CaesarLock")
root.geometry("800x400")
root.resizable(False, False)

# Icon
icon = tk.PhotoImage(file="./assets/icon.png")
root.iconphoto(False, icon)

# Image Path Entry
tk.Label(root, text="Image Path:").pack(pady=5)
image_path_entry = tk.Entry(root, width=50)
image_path_entry.pack(pady=5)
tk.Button(root, text="Browse", command=browse_image).pack(pady=5)

# Key Entry
tk.Label(root, text="Encryption/Decryption Key:").pack(pady=5)
key_entry = tk.Entry(root, width=50)
key_entry.pack(pady=5)

# Buttons
tk.Button(root, text="Encrypt Image", command=on_encrypt).pack(pady=5)
tk.Button(root, text="Decrypt Image", command=on_decrypt).pack(pady=5)

# Console Output Text Widget
console_output = tk.Text(root, height=6, width=70)
console_output.pack(pady=10)

insert_console_output('Welcome to CaesarLock')

root.mainloop()