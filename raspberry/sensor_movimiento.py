import RPi.GPIO as GPIO    					# Importamos la libreria GPIO
import time                					# Importamos time
from time import gmtime, strftime  				# importamos gmtime y strftime
GPIO.setmode(GPIO.BCM)             				# Configuramos los pines GPIO como BCM
PIR_PIN = 7                        				# Usaremos el pin GPIO 07
GPIO.setup(PIR_PIN, GPIO.IN)       				# Lo configuramos como entrada
 
#GPIO.setup(17, GPIO.OUT)          				# Configuramos el pin 17 como salida (para un led)
 
try:
	while True:  						# Iniciamos un bucle infinito
		if GPIO.input(PIR_PIN):  			# Si hay segnal en el pin GPIO 07
#           	GPIO.output(17,True) 				# Encendemos el led
			time.sleep(1)        									# Pausa de 1 segundo
			timex = strftime("%d-%m-%Y %H:%M:%S", gmtime()) # Creamos una cadena de texto con la hora
			print timex + " MOVIMIENTO DETECTADO"  	# La sacamos por pantalla
			time.sleep(0.1)  											# Pausa de 1 segundo
#           GPIO.output(17,False)  				# Apagamos el led
		time.sleep(1)              			# Pausa de 1 segundo y vuelta a empezar
except KeyboardInterrupt:               			# Si el usuario pulsa CONTROL + C...
        print "\nSaliendo ...\n" 					# Anunciamos que finalizamos el script
        GPIO.cleanup()         					# Limpiamos los pines GPIO y salimos
