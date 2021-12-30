#!/usr/bin/python3

import socket,argparse,sys
from pwn import *

parser = argparse.ArgumentParser(description="Obten la IP de un dominio")
parser.add_argument('-t','--target',help="Introduce la URL")
parser = parser.parse_args()


def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

def main():

	if parser.target:

		try:
			print("\n %s - IP %s " %(parser.target, socket.gethostbyname(parser.target)))

		except:

			print("No se econtró el dominio")
	else:
		print("\n[!] Error al ejecutar el script: python3 domainToIp.py -t url")

if __name__ == '__main__':

	main()
