# ppmcrypt
# This is just a conceptual test 
#
#
# XOR CIPHER: <https://en.wikipedia.org/wiki/XOR_cipher>

#  a^b^b = a ---- simple XOR cipher technique used!

def read_ppm(path):
    """
    Read a P3 (ASCII) PPM file and return (width, height, max_val, pixels)
    pixels is a list of (R,G,B) tuples
    """
    with open(path, "r") as f:
        lines = f.readlines()

    # Remove comments and empty lines
    lines = [line.strip() for line in lines if line.strip() and not line.startswith("#")]

    if lines[0] != "P3":
        raise ValueError("Only P3 PPM format supported")

    # Read width, height
    width, height = map(int, lines[1].split())
    # Max color value
    max_val = int(lines[2])

    # All remaining numbers are pixels
    pixel_values = []
    for line in lines[3:]:
        pixel_values.extend(map(int, line.split()))

    if len(pixel_values) != width * height * 3:
        raise ValueError("Pixel data does not match width*height*3")

    # Group into (R,G,B) tuples
    pixels = [(pixel_values[i], pixel_values[i+1], pixel_values[i+2])
              for i in range(0, len(pixel_values), 3)]

    return width, height, max_val, pixels


"""
def read_ppm(path):

    with open(path, "r") as f:
        tokens = f.read().split()

    if tokens[0] != "P3":
        raise ValueError("Only P3 PPM Format Supported!")

    width = int(tokens[1])
    height = int(tokens[2])
    max_val = int(tokens[3])

    pixel_data = list(map(int,tokens[4:]))

    if len(pixel_data) != width*height*3:
        raise ValueError("Invalid Pixel Data Length!")

        pixels = [(pixel_data[i], pixel_data[i+1], pixel_data[i+2])
                    for i in range(0, len(pixel_data), 3)]
    
    
    return width, height, max_val, pixels

"""







def pixel_keystream(pixels):
    """ Yeild a byte stream from pixel RGB values!"""
    for r,g,b in pixels:
        yield (r + g + b) % 256

def encrypt(message: bytes, pixels):
    """Encrypt a message using PPM pixels!"""

    stream = list(pixel_keystream(pixels))
    encrypted = bytearray()

    for i , byte in enumerate(message):
        key = stream[i % len(stream)]
        encrypted.append(byte ^ key)

    return bytes(encrypted)

def decrypt(ciphertext: bytes, pixels):
    """Decrypt a message using PPM pixles!!"""
    return encrypt(ciphertext, pixels)


