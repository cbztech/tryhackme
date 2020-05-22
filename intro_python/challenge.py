from base64 import *

with open('C:/tryhackme/encodedflag.txt', 'r') as encoded_file:
    decode = encoded_file.read()
    loop_count = 1

    while loop_count < 15:
            if loop_count <= 5:
                # Base 16 decoding
                while loop_count <= 5:
                    decode = b16decode(decode)
                    loop_count +=1
            elif loop_count > 5 and loop_count <= 10:
                # Base 32 decoding
                while loop_count <= 10:
                    decode = b32decode(decode)
                    loop_count +=1
            elif loop_count > 10 and loop_count <= 15:
                # Base 64 decoding
                while loop_count <= 15:
                    decode = b64decode(decode)
                    loop_count +=1

    print('The final decoded string is :\n' + str(decode))
