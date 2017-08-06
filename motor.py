#Motor a pasos con parametros desde shell

import sys
import RPi.GPIO as GPIO
import time
import led

def motor(direccion1, pasos1, espera1, direccion2, pasos2, espera2):
    print("MOTOR 1 hacia la {}, {} pasos y Espera de {}s".format(direccion1, pasos1, espera1))
    print("MOTOR 2 hacia la {}, {} pasos y Espera de {}s".format(direccion2, pasos2, espera2))
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(14, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    
    if direccion1 == 'izq':
        GPIO.output(23, True)
    elif direccion1 == 'der':
        GPIO.output(23, False)
    if direccion2 == 'izq':
        GPIO.output(14, True)
    elif direccion2 == 'der':
        GPIO.output(14, False)

    led.edo(True)

    ContadorPasos1 = 0
    ContadorPasos2 = 0

    while ContadorPasos1 < pasos1:

        GPIO.output(24, True)
        time.sleep(espera1)
        GPIO.output(24, False)
        ContadorPasos1 +=1

        time.sleep(espera1)

    while ContadorPasos2 < pasos2:

        GPIO.output(15, True)
        time.sleep(espera2)
        GPIO.output(15, False)
        ContadorPasos2 +=1

        time.sleep(espera2)

    GPIO.cleanup()
    
    
    

