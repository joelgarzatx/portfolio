inp = input('Message: ')
secret_code = ''
for c in inp:
    secret_code += chr(ord(c) + 1)    
print(secret_code[::-1])