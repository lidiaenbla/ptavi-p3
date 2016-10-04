#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
from smallsmilhandler import SmallSMILHandler

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    fichero = sys.argv[1]
    parser.parse(open(fichero))
    misdatos = cHandler.get_tags()
    for etiqueta in misdatos:
    	elemento = etiqueta.items() #es un diccionario
    	print(elemento)
