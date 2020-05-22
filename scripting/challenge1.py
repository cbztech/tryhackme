from base64 import *

with open('C:/tryhackme/b64.txt', 'r') as encoded_file:
    decode = encoded_file.read()

    count = 1

    while count <= 50:
        decode = b64decode(decode)
        count +=1
    
    print(str(decode))