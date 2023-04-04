import re
# cadena = input("Ingrese cadena a verificar: ")
#a cc b

tokens={}
numeros=['1','2','3','4','5','6','7','8','9','0','-1','-2','-3','-4','-5','-6','-7','-8','-9']
operadores=["*","+","|","?"]
variables =['var','let']

with open('entrada1.txt', 'r') as file:
    for line in file:
        text=line
        inside_block_comment = False  # flag to keep track of whether we're inside a block comment or not
        
        
        # print("Identificador")
        # fila = "var + 5 * -11 = otraVariable + 2"
        tickets = line.split()
        # print(tickets)
        for token in tickets:
            # print(token)
            """ if token in operadores:
                print("operador")
            elif token in numeros:
                print("Numero")
            elif token == "=":
                print("operador de asignacion")
            elif token in variables:
                print("Identificador") """
            if any(op in token for op in operadores):
                print("Operador")
            elif any(num in token for num in numeros):
                print("Numero")
            elif token == "=":
                print("Operador de asignacion")
            elif any(var in token for var in variables):
                print("Identificador")

            # aqui verifica si es un comentario
            elif line.startswith("/*"):
                if inside_block_comment:
                    #si estamos en un bloque de comentario, revisar si alli termina o sigue
                    if '*/' in line and inside_block_comment or '*)' in line and inside_block_comment:
                        inside_block_comment = False  # found the end of the comment
                else:
                    #revisar si comienza el bloque de comentario
                    if '/*' in line or '(*' in line:
                        inside_block_comment = True  # found the start of a comment
                    else:
                        #si no se esta en un comentario, continuar
                        pass
            else:
                pass
            # elif line.startswith(numeros):
            #     print("Error lexico, token no reconocido")
            #     exit()

            


    

