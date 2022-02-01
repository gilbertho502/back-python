#importando solo la funcion gTTS del modulo
from gtts import gTTS
import os
#texto que reproducira el audio
mytexto = "python es muy amigable"
#cambiando el lenguaje
lenguaje = "es"
convertir = gTTS(text= mytexto, lang = lenguaje, slow=False)
#salvar la conversion de texto a un audio
convertir.save("cargamos.mp3")
os.system("start cargamos.mp3")