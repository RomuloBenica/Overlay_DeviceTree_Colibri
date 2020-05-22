#!/usr/bin/python3
#escrita e leitura da uart2 placa colibri imx7

import sys
import serial
import pynmea2
import time


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
        while True:
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
    escreverNaUart(uart2)
    time.sleep(2)
    lerUart(uart2)
