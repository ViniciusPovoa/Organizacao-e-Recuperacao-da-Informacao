#código python para calcular raizes de equações de segundo grau

a = input("Entre com o valor do coeficiente a: ")
a = float(a) #converte a string lida para float
b = float( input("Entre com o valor do coeficiente b: ") )
c = float( input("Entre com o valor do coeficiente c: ") )

if a == 0:
    print("Não é uma equação de segundo grau");
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Não tem raizes reais")
    elif delta == 0:
        raiz = -b/(2*a)
        print("Raiz real: ", raiz)
    else:  #delta > 0
        raiz1 = (-b + delta**0.5)/(2*a);
        raiz2 = (-b - delta**0.5)/(2*a);
        print('Raiz 1: ', raiz1, 'Raiz 2:', raiz2 );

print('Tenha um bom dia!')