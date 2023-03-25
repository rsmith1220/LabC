import re
cadena = input("Ingrese cadena a verificar: ")
#a cc b



with open('ejemplo.txt', 'r') as file:
    for line in file:
        text=line
        # Input text
        # text = "let token1 = 'a'|'b'\nlet token2 = 'c'*
        regex = r'^let\s+(\w+)\s+=\s+(.*)$'

        matches = re.findall(regex, text, re.MULTILINE)

        for match in matches:
            name = match[0]
            value = match[1].strip()
            print(name, value)

for token in cadena:
    if token == 'a':
        print('token1')
    elif token == 'b':
        print('token1')
    elif token == 'c':
        print('token2')
    else:
        pass
