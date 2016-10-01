#!/usr/bin/python
import RPi.GPIO as GPIO
import time

led1 = 21
led2 = 18
# ------------------7  8 10 11 12 13 15 16
codeNumber = {' ': (1, 1, 1, 1, 1, 1, 1, 0),
              '0': (1, 0, 0, 0, 0, 0, 0, 1),
              '1': (1, 0, 1, 1, 0, 1, 1, 1),
              '2': (1, 1, 0, 0, 0, 1, 0, 0),
              '3': (1, 0, 0, 1, 0, 1, 0, 0),
              '4': (1, 0, 1, 1, 0, 0, 1, 0),
              '5': (1, 0, 0, 1, 1, 0, 0, 0),
              '6': (1, 0, 0, 0, 1, 0, 0, 0),
              '7': (1, 0, 1, 1, 0, 1, 0, 1),
              '8': (1, 0, 0, 0, 0, 0, 0, 0),
              '9': (1, 0, 0, 1, 0, 0, 0, 0),
              'A': (1, 0, 1, 0, 0, 0, 0, 0),
              'H': (1, 0, 1, 0, 0, 0, 1, 0),
              'O': (1, 0, 0, 0, 0, 0, 0, 1),
              'L': (1, 1, 0, 0, 1, 0, 1, 1)}
              

pines = {7, 8, 10, 11, 12, 13, 15, 16}

caracteres = {'0','1','2','3','4','5',
              '6','7','8','9','A'}
##hola = {'H','O','L','A'}
hola = 'HOLA'

GPIO.setmode(GPIO.BOARD)

for pin in pines:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,GPIO.HIGH)

for caracter in hola:
    
    pinValues = codeNumber[caracter]
    pos = 0
    for pin in pines:
        print(pin)
        pinValue = pinValues[pos]
        print(pinValue)
        GPIO.output(pin, pinValue)
        pos = pos+1
    time.sleep(1.5)


##for pin in pines:
##    GPIO.output(pin,GPIO.LOW)


try:
    while True:
        pass
except KeyboardInterrupt:
    GPIO.cleanup()
