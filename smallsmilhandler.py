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
		self.src = ""
		self.region = ""
		self.begin = ""
		self.dur = ""

	def startElement(self,name,attrs):
		if name == 'root-layout':
            self.width = attrs.get('width',"") 
            self.heigth = attrs.get('heigth',"") 
            self.backgroundcolor = attrs.get('background-color',"") 
        elif name == 'region':
            self.id = attrs.get('id',"") 
            self.top = attrs.get('top',"") 
            self.left = attrs.get('left',"") 
        elif name == 'img':
        	self.src = attrs.get('src',"") 
            self.region = attrs.get('region',"") 
            self.begin = attrs.get('begin',"") 
            self.dur = attrs.get('dur',"") 
        elif name == 'audio':
        	self.src = attrs.get('src',"") 
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"") 
        elif name == 'textstream':
        	self.src = attrs.get('src',"")
     def endElement(self, name): #el parser lo llama cada vez que encuentre una etiqueta de cierre
        """
        Método que se llama al cerrar una etiqueta
        """
        if name == 'root-layout':
            print(self.width + "/" + self.heigth + "/" + self.backgroundcolor)
      


	def get_tags (self):
		return self.misdatos

if __name__ == "__main__":

	parser = make_parser()
	cHandler = SmallSMILHandler()
	parser.setContentHandler(cHandler)