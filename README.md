# Pixel-Powered Encryption (Python Demo)

This is a **Python prototype** exploring a fun concept: **using an image as the encryption key**. The idea is simple:

- A **PPM image** (plain-text RGB image) acts as the key.
- Each pixel’s RGB values are transformed into a **keystream**.
- The message bytes are combined with the keystream using **XOR**, producing an encrypted message.
- To decrypt, you need the **exact same image**.

> ⚠️ **Note:** This is purely a **concept and learning project**. It is **not cryptographically secure**.  
> The current implementation is a Python demo. A proper library may be written in C++ in the future for performance, handling large images, and binary PPM support.

---

## Features

- Reads **P3 (ASCII) PPM images** as keys.
- Encrypts and decrypts messages using pixel-based XOR.
- Easy to understand and modify — perfect for experimentation.
- Highlights how **digital media can function as a key**.

---

## How It Works

1. Convert the PPM image into a list of `(R, G, B)` tuples.
2. Collapse the RGB values into a **single byte**: `(R+G+B) % 256`.
3. Create a **keystream** by iterating over the pixels.
4. XOR each message byte with the corresponding key byte (looping if message is longer than the number of pixels).
5. Decrypt by repeating the same process with the same image.

Even a **single pixel change** will break decryption — the image is literally your key.

---

## Usage Example

```python
from ppmcrypt import read_ppm, encrypt, decrypt

# Load PPM key
width, height, max_val, pixels = read_ppm("examples/key.ppm")

# Original message
message = b"Hello from the pixel vault!"

# Encrypt
cipher = encrypt(message, pixels)
print("Encrypted (hex):", cipher.hex())

# Decrypt
plain = decrypt(cipher, pixels)
print("Decrypted:", plain.decode())

