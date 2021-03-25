def suma(n1,n2):
    print(str(n1)+" + "+str(n2)+" = "+str(int(n1)+int(n2)))

def resta(n1,n2):
    print(str(n1)+" - "+str(n2)+" = "+str(int(n1)-int(n2)))

def multi(n1,n2):
    print(str(n1)+" * "+str(n2)+" = "+str(int(n1)*int(n2)))

def divicion(n1,n2):
    print(str(n1)+" / "+str(n2)+" = "+str(int(n1)/int(n2)))

def aux():
    print("1)Seguir jugando \n2)Fin")
    op = int(input(">> "))
    if op == 1:
        print("Ok")
        return 1
    elif op == 2:
        print("Fin")
        return 5
    else:
        print("Esa opcion no existe")
        aux()
