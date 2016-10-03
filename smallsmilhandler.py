#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):

        self.width = ""
        self.heigth = ""
        self.backgroundcolor = ""
        self.id = ""
        self.top = ""
        self.left = ""
        self.right = ""
        self.isrc = ""
        self.asrc = ""
        self.tsrc = ""
        self.region = ""
        self.begin = ""
        self.dur = ""
        self.misdatos = []
       

    def startElement(self,etiqueta,attrs):

        if etiqueta == 'root-layout':
            rootlayout = {'width' : attrs.get('width',""),'height' : attrs.get('height',""),'background-color': attrs.get('background-color')}
            self.misdatos.append(rootlayout)
        elif etiqueta == 'region':
            region = {'id' : attrs.get('id', ""), 'top' : attrs.get('top', ""), 'bottom' : attrs.get('bottom',""), 'left' : attrs.get('left', ""),'right' : attrs.get('right',"")}
            self.misdatos.append(region)
        elif etiqueta == 'img':
            img = {'isrc' : attrs.get('src', ""), 'iregion' : attrs.get('region', ""),'ibegin' : attrs.get('begin', ""), 'idur' : attrs.get('dur', "")} 
            self.misdatos.append(img)
        elif etiqueta == 'audio':
            audio = {'asrc' : attrs.get('src', ""), 'abegin' : attrs.get('begin', ""), 'adur' : attrs.get('dur', "")} 
            self.misdatos.append(audio)
        elif etiqueta == 'textstream':
            textstream = {'tsrc' : attrs.get('src',"")}
            self.misdatos.append(textstream)



    def get_tags (self):
        return self.misdatos

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    misdatos = cHandler.get_tags()
    for i in misdatos:
        print(i)
        print("\n")