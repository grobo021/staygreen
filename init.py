#!/usr/bin/env python3
import ADC0832
import requests
import time

def init():
	ADC0832.setup()

def loop():
	while True:
		res = ADC0832.getResult()
		moisture = 255 - res
		requests.get(f'https://api.thingspeak.com/update?api_key=P2IGUNXT8NQECGEP&field1={moisture}')
		time.sleep(60)

if __name__ == '__main__':
	init()
	try:
		loop()
	except KeyboardInterrupt: 
		ADC0832.destroy()
		print('The end !')
