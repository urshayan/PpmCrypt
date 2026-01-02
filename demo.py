from ppmcrypt import read_ppm, encrypt, decrypt

width , height, max_val, pixles = read_ppm("examples/key.ppm")

# original messaage
message = b"Hello from PPMCRYPT"

#encrypt
cipher = encrypt(message, pixles)

print("Encrypt (hex) : " , cipher.hex())

print("\n Now decrypting!! \n")

#decrypt
plain = decrypt(cipher, pixles)

print("Decrypted: " , plain.decode())


