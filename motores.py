#Motor a pasos con parametros desde shell

import sys, time, led, SexaToDeg1
import RPi.GPIO as GPIO

class motores(self, grados):        

    def Coordenadas(self, coordenadas):
        print("Escibe las coordenadas del astro:" )
        coordenadas = raw_input()
        return coordenadas

    def PasarCoord():
        SexaToDeg1.astro(self.Coordenadas)
                

    def motor(self, pasos1, pasos2):
        print("MOTOR 1 hacia la {}".format(pasos1))
        print("MOTOR 2 hacia la {}".format(pasos2))
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
        espera = 0.01
        ContadorPasos1 = 0
        ContadorPasos2 = 0

        while ContadorPasos1 < pasos1:

            GPIO.output(24, True)
            time.sleep(espera)
            GPIO.output(24, False)
            ContadorPasos1 +=1

            time.sleep(espera)

        while ContadorPasos2 < pasos2:

            GPIO.output(15, True)
            time.sleep(espera)
            GPIO.output(15, False)
            ContadorPasos2 +=1

            time.sleep(espera)

        GPIO.cleanup()
    
    
    

