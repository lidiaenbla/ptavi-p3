#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import json
import urllib.request
from smallsmilhandler import SmallSMILHandler


class KaraokeLocal():
    def Inicializador(self, fichero):
        self.cHandler = SmallSMILHandler()
        self.misdatos = []
        self.fich = fichero

        parser = make_parser()
        parser.setContentHandler(self.cHandler)
        parser.parse(open(self.fich))
        misdatos = self.cHandler.get_tags()

        return misdatos

    def toStr(self, datos):
        exit = ""

        for elementos in datos:
            for etiqueta in elementos:
                for atributo, valor in elementos[etiqueta].items():
                        exit = exit + '\t' + atributo + ' = "' + valor + '"\t'
            print(etiqueta + exit)
            exit = ""

    def do_local(self, datos):
        exit = ""
        for elementos in datos:
            for etiqueta in elementos:
                for atributo, valor in elementos[etiqueta].items():
                    if (atributo == 'src') and (valor[0:7] == 'http://'):
                        valorN = valor.split("/")[-1]
                        urllib.request.urlretrieve(valor, valorN)
                        exit = exit + '\t' + atributo + '="' + valorN + '"\t'
                    else:
                        exit = exit + '\t' + atributo + ' = "' + valor + '"\t'
            print(etiqueta + exit)
            exit = ""

    def do_joson(self, datos):
        json.dump(datos, open('karaoke.json', 'w'))

if __name__ == "__main__":

    objKaraokeLocal = KaraokeLocal()
    datos = []

    try:
        fichero = sys.argv[1]
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")

    datos = objKaraokeLocal.Inicializador(fichero)
    objKaraokeLocal.toStr(datos)
    objKaraokeLocal.do_local(datos)
    objKaraokeLocal.do_joson(datos)
    objKaraokeLocal.toStr(datos)
