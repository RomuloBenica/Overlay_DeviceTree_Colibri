#!/usr/bin/python3
import sys
import serial
import pynmea2
import time
import os.path
import os

GPIO_PATH = "/sys/class/gpio"
serial_port2 = "/dev/ttymxc1"
#serial_port3 = "/dev/ttymxc2"
#serial_port4 =  "/dev/ttymxc3"
#serial_port5 =  "/dev/ttymxc4"
#serial_port6 =  "/dev/ttymxc5"


if len(sys.argv) > 1:
    serial_port = sys.argv[1]

uart2 = serial.Serial(serial_port2,500000, 8, 'N', 1)
#uart3 = serial.Serial(serial_port3,115200, 8, 'N', 1)
#uart4 = serial.Serial(serial_port4,9600, 8, 'N', 1)

def lerUart(uart):
    contador = 0 
    arrValorLido = [] 
    mensagemRecebida = []
    try:
        #exportFile = open(GPIO_PATH+'/export', 'w')
        #unexportFile = open(GPIO_PATH+'/unexport', 'w')
        direcaoGpio = open(GPIO_PATH+'/gpio139/direction', 'r')
        direcaoGpio.write('out')
        direcaoGpio.flush()
        valorGpio = open(GPIO_PATH+'/gpio139/value', 'w')
        print(direcaoGpio)
        while True:
            valorGpio.write('0')
            valorGpio.flush()

            if uart.in_waiting > 0:
                valorLido = uart.read()
                arrValorLido.append(valorLido)
                contador += 1

                if  valorLido == b'X':

                    for i in range (contador):
                        valorGpio.write('1')
                        valorGpio.flush()
                        mensagemRecebida.append(arrValorLido.pop(0))

                    mensagemString = str(mensagemRecebida)
                    print('Mensagem lida :'+ mensagemString.strip('[]'))
                    mensagemRecebida.clear()
                    contador = 0
    except serial.SerialException:
        print('Erro ao ler Uart:')

def escreverNaUart(uartEscreve):
    try:
        x = 0
        while x < 3:
            x +=1
            uartEscreve.flushInput()
            uartEscreve.flushOutput()
            uartEscreve.write(b'INITPROX')
            
    except:
        print('Erro ao escrever na uart')

if __name__ == '__main__':
    print('Inicio de leitura e escrita das uarts ...')
    #escreverNaUart(uart2)
    #time.sleep(5)
    lerUart(uart2)