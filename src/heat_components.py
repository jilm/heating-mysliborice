# -*- coding: utf-8 -*-

class TQS3:
    type = 'TQS3'
    label = 'BT'
    def __init__(self, spinel_address = 49):
        pass

class PT100:
    type = "PT100"
    short = "Thermistor"
    label = "BT"
    def __init__(self, 
        short_desc = None):

        self.short_desc = short_desc
        pass
    
    
class P5310:
    type = "P5310"
    short = "Temperature Current Converter"
    # output range: 0-60 stC

class Quido88:
    type = 'Quido 8/8'
    short = 'Binary IOs and temperature measurement'
    def __init__(self, spinel_address = 49):
        pass
    
class AD4ETH:
    type = 'AD4ETH'
    short = 'AD converter with ethernet connection'
    
class DA2RS:
    type = 'DA2RS'
    short = 'DA converter with RS485'
    long = """Univerzální převodník s analogovým výstupem při řízení
              a regulaci. Dva nezávislé analogové výstupy mohou být
              buď napěťové nebo proudové. Hodnoty pro analogové výstupy
              zasílá nadřazený systém přes rozhraní RS232 nebo RS485."""
#    gates = {
#        'out1' :
#        'out2' :
#        'comm' :
#        'pwrs' :
#    }
    
class GNOME:
    type = 'GNOME'
    short = 'RS485 to ETHERNET'
    
class SENSYCON:
    type = 'SENSYCON'
    short = 'PT100 to current converter'
    # output range 0-100 dgC
    
class Rele:
    type = 'Rele'
    short = 'Rele'
        
components = {        
    
    # Čidlo pro měření teploty vody na výstupu z kotle
    '=KK-BTH' : PT100(
        short_desc = """Senzor teploty média na výstupu z krbových kamen."""
    ),
    
    '-B3' : P5310(),
    
    '+204-BT' : TQS3(
        spinel_address = 12,
    ),
    
    '+0-BT' : TQS3(
        ),
        
    '-B1' : Quido88(
        spinel_address = 0x34 # 34h
    ),

    '-B2' : Quido88(
        spinel_address = 0x35 # 35h
    ),

    '-B3' : AD4ETH(),
    '-B4' : DA2RS(),
    '-B5' : GNOME(),
    '-B6' : SENSYCON(),
    '-B7' : P5310(),
    '-K1' : Rele(),
    '-K2' : Rele(),
    '-K3' : Rele(),
    '-K4' : Rele(),
    '-K5' : Rele(),
    '-K6' : Rele(),
    '-K7' : Rele(),
    '-K8' : Rele(),
    '-K9' : Rele(),

}        


for c in components:
    print('{} & {} & {}\\\\'.format(c, components[c].type, components[c].short_desc))


