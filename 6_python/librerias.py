import random
from datetime import date, datetime
import math
import statistics
cargamos = ["alicia", "carlos", "javier", "maria",  "nicolle"]

# print(random.choice(cargamos))
# print(random.randrange(90,100))

#devuelve la fecha del sistema
hoy = date.today()
fecha_hora = datetime.now()
# print(hoy)
# #devuelve fecha y hora del sistema
# print(fecha_hora)

# print(hoy.month)
# print(hoy.day)
# print(hoy.year)

# print(f"La hora actual es: {fecha_hora.hour}")
# print(f"El minuto actual es: {fecha_hora.minute}")
# print(f"Los segundos son: {fecha_hora.second}")

print(math.pi)
# print(math.cos(math.pi/4))

notas = [19,17,20,17,20,14,19,20]
#promedio
print(statistics.mean(notas))
#moda
print(statistics.mode(notas))
#valor medio
print(statistics.median(notas))