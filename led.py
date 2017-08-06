import RPi.GPIO as GPIO

def edo(n):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, n)

#if __name__ == '__main__':
 #   import sys
  #  edo(str(sys.argv[0]))
