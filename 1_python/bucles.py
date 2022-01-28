for i in range(10):
    print(f"{i +1} hola mundo")

for i in range(1,10, 2):
    print(i)

x = 0
while x<=100:
    print(x)
    x += 1

contrasena = "python"
cont = 0
while True:
    con = input("Ingrese constraseña: ")
    if con == contrasena:
        print("contraseña correcta")
        break
    else:
        print("contraseña equivocada")
        cont = cont+1
        if cont == 3:
            print("Supero los intentos, vuelva en 10 minutos")
            break
        