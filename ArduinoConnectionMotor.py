import pyfirmata
import time

comPort = 'COM3'
board = pyfirmata.Arduino(comPort)
paso = board.get_pin('d:2:o')
dire = board.get_pin('d:5:o')
habi = board.get_pin('d:8:o')
retardo = 0.001
tiempo = 10

class ValueOfLight:
    def ledLight(val):
        habi.write(0)
        if val == 1:
            dire.write(0)
            for i in range(tiempo):
                paso.write(1)
                time.sleep(retardo)
                paso.write(0)
                time.sleep(retardo)
        elif val == 2:
            dire.write(1)
            for i in range(tiempo):
                paso.write(1)
                time.sleep(retardo)
                paso.write(0)
                time.sleep(retardo)
        elif val == 3:
            dire.write(1)
            for i in range(tiempo):
                paso.write(1)
                time.sleep(retardo*2)
                paso.write(0)
                time.sleep(retardo*2)
        else:
            paso.write(0)
            dire.write(0)
            habi.write(0)

