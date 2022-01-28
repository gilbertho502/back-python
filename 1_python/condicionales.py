# num1 = int(input("ingrese el primer numero: "))
# num2 = int(input("ingrese el segundo numero: "))

# if num1 > num2:
#     print(f"El numero mayor es {num1}")
# elif num1 == num2:
#     print("Los numeros son iguales")
# else:
#     print(f"el numero mayor es: {num2}")

candidato = input("Elija su candidato: ")
if candidato.upper() =="A" or candidato.upper()=="D":
    print("Usted voto por el partido rojo")
elif candidato.upper() =="B":
    print("Usted voto por el partido azul")
elif candidato.upper() =="C":
    print("Usted voto por el partido verde")
else:
    print("Opcion No valida")