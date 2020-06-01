from punto import Punto, Rectangulo

print("\nEjercicio Coordenadas")
stop = False
while stop == False:
    
    print('''
¿Qué opción deseas ingresar?:

- 1: Agregar un punto de coordenadas.
- 2: Mostrar su punto.
- 3: Consulte el cuadrante donde se ubica su punto.
- 4: Crear un vector con un segundo punto.
- 5: Para crear un rectangulo.
- 6: Para salir del menu.
    ''')

    option = int(input())
    if option == 1:
        print('Ingrese su punto (x,y)')
        print('Ingrese X')
        X = int(input())
        X = float(X) if X != '' else 0
        print('Ingrese Y')
        Y = input()
        Y = float(Y) if Y != '' else 0
        coordenada = Punto(X,Y)
    elif option ==2:
        impresion = coordenada.Imprimir()
        pass
    elif option ==3:
        cuadrante = coordenada.CalculoCuadrante()
    elif option == 4:
        print('Ingrese el segundo punto (X2,Y1)')
        print('Ingrese X1:')
        Z = input()
        Z = float(Z) if Z != '' else 0
        print('Ingrese Y1')
        W = input()
        W = float(W) if W != '' else 0
        vector = coordenada.Vectorizador(Z,W)
        pass
    elif option ==5:
        rectangulo = Rectangulo(a=X,b=Y,a1=Z,b1=W)
        rectangulo.base()
        rectangulo.altura()
        rectangulo.area()
        pass
    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        print("Not implemented yet or invalid option "+str(option))


