try:
    suma = 20 + 15
except Exception as error:
    #cuando encuentra un error, etra a este bloque
    print(f"ha ocurrido un error {error}")
else:
    #cuando no hay error
    print("No ha existido ninguna excepcion")
finally:
    #siempre se ejecuta
    print("se termino el codigo")