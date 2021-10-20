import xml.etree.ElementTree as ET
from xml.dom import minidom
import lista
import re

class Carga_Archivo:
    var=lista.lista_doble()

    def __init__(self):

        self.carga(r"C:\Users\Administrator\Desktop\proyecto 3\prueba.xml")
        

    # def cargaArchivo(self,link):

    #     tree=ET.parse("prueba.xml")
    #     self.rootM=tree.getroot()
        
    #     self.analizarArchivo()

    def carga(self,link):
        archivo = open(link, 'r')           
        self.archivo=archivo.read()
            
        if (self.archivo.isspace() or len(self.archivo) <= 1):
                print("Error de archivo")
        else:
            #print(self.archivo)
            self.separar()

    def separar(self):
        self.lista = re.split('<|>|=|/|'+chr(32)+'|'+chr(9)+'|'+chr(34)+'|\n|""',self.archivo) 

        for x in self.lista:
            print(x)
            

    def analizarArchivo(self):

        for elem in self.rootM:
            for subelem in elem:
                print(subelem.tag)
                print(subelem.text)

                #for sub2 in subelem:

    def verificar(self):
        lista=["TIEMPO","REFERENCIA","NIT_EMISOR","NIT_RECEPTOR","VALOR","IVA","TOTAL","DTE","SOLICITUD_AUTORIZACION"]



cosa = Carga_Archivo()