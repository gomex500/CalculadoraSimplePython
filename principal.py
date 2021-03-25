import funciones as fn
import funMenu as fm
op = 0
while(op!=5):
    n1 = fm.numero1()
    n2 = fm.numero2()
    op = fm.op()
    op = int(op)
    if op == 1:
        fn.suma(n1,n2)
        op = fn.aux()
        op = int(op)
    elif op == 2:
        fn.resta(n1,n2)
        op = fn.aux()
        op = int(op)
    elif op == 3:
        fn.multi(n1,n2)
        op = fn.aux()
        op = int(op)
    elif op == 4:
        fn.divicion(n1,n2)
        op = fn.aux()
        op = int(op)
    elif op == 5:
        print("Fin \n")
    else:
        op = fn.aux()
        op = int(op)
