#Programa para motor a paso basado en
#
#
#
import sys
import RPi.GPIO as gpio
import time
import led

class motor:

    def __init__(self, direccion, pasos, TiempoEspera):
        self.direccion = direccion
        self.paoss = pasos
        self.TiempoEspera = (self, direccion, pasos,TiempoEspera)


#try:
  #  direccion = sys.argv[1]
 #   pasos = int(float(sys.argv[2]))
 #   TiempoEspera = float(sys.argv[3])
#except:
    #pasos = 0

    #print("hacia la %s, %s pasos y Espera de %s s") % (direccion, pasos, TiempoEspera)

    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)
#gpio.setup(25, gpio.OUT)
#gpio.setup(18, gpio.IN, pull_up_down=gpio.PUD_UP)

#inicio = gpio.input(18) 

#while True:
    #inicio == True
   # if inicio == False: 
    if direccion == 'izq':
        gpio.output(23, True)
    elif direccion =='der':
        gpio.output(23, False)

        led.edo(True)

    ContadorPasos = 0



    while ContadorPasos < pasos:

        gpio.output(24, True)
        time.sleep(TiempoEspera)
        gpio.output(24, False)
        ContadorPasos +=1

        time.sleep(TiempoEspera)

    gpio.cleanup()

