#Motor a pasos con parametros desde shell

import sys, SexaToDeg, led, time
import RPi.GPIO as GPIO

def motor(coordenadas):
    pasos1, pasos2 = ObtPasos(coordenadas)
    print("*MOTOR RA {} pasos                                              *".format(pasos1))
    print("*MOTOR DEC {} pasos                                             *".format(pasos2))
    print("*****************************************************************")
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(14, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)   
    GPIO.output(23, True)
    GPIO.output(14, True)
    ContadorPasos1 = 0
    ContadorPasos2 = 0
    while ContadorPasos1 < pasos1:
        GPIO.output(24, True)
        time.sleep(0.05)
        led.edo(True)
        GPIO.output(24, False)
        ContadorPasos1 +=1
        time.sleep(0.05)
        led.edo(False)
    time.sleep(1)
    while ContadorPasos2 < pasos2:
        GPIO.output(15, True)
        time.sleep(0.05)
        led.edo(True)
        GPIO.output(15, False)
        ContadorPasos2 +=1
        time.sleep(0.05)
        led.edo(False)
        
    GPIO.cleanup()
    return pasos1, pasos2 
    
def ObtPasos(coordenadas):
    pasos1, pasos2 = SexaToDeg.DegToPasos(coordenadas)
    return pasos1, pasos2

#def Home(coordenadas):
    
