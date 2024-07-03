from PIL import Image
import numpy as np
import tkinter as tk 

def insert_console_output(text):
    console_output.insert(tk.END, text + "\n")
    console_output.see(tk.END)

def encrypt_images(image_path, key):
    base_image = Image.open(image_path)
    img_array = np.array(base_image)

    np.random.seed(key)
    key_array = np.random.randint(0, 256, img_array.shape, dtype=np.uint8)

    encrypt_array = (img_array + key_array) % 256
    encrypt_image = Image.fromarray(encrypt_array)
    encrypt_image.save("encrypted_image.png")
    print("Your Image has been encrypterd")

def decrypt_images(image_path, key):
    base_image = Image.open(image_path)
    img_array = np.array(base_image)

    np.random.seed(key)
    key_array = np.random.randint(0, 256, img_array.shape, dtype=np.uint8)

    decrypt_array = (img_array - key_array) % 256
    decrypt_image = Image.fromarray(decrypt_array)
    decrypt_image.save("decrypted_image.png")
    print("Your Image has been decrypted")

key = ()

