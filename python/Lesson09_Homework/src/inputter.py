f = open('v:/inputter.txt','a')
f.close()

filetext = open('v:/inputter.txt','r').read()
print(filetext)

string_input = 'Enter text: '
while True:
    inp = input(string_input)
    if inp == '':
        break
    else:
        f = open('v:/inputter.txt','a')
        f.write(inp)
        f.close()
        filetext = open('v:/inputter.txt','r').read()
        print(filetext)
        
        