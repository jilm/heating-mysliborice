# -*- coding: utf-8 -*-

components = {}

def register(component):
    components[component.label] = component

class Gate:
    pass
    
class ResistorGate(Gate):
    pass

class Component:
    def __init__(self, label):
        self.label = label
        register(self)

class PT100(Component):
    
    type = "PT100"
    short = "Thermistor"
    label_base = "BT"
    terminals = (':1', ':2')
    
    def __init__(self, label):
        super().__init__(label)        
    
class P5310(Component):

    type = 'P5310'
    manufacturer = 'JSP'
    short = 'Převodní teplota na proudovou smyčku.'
    temp_range = (0.0, 60.0)    # rozsah teplot [degC]
    out_range = (4e-3, 20e-3)   # rozsah výstupních proudů [A]
    terminals = (':1', ':2', ':3', ':4', ':5', ':6', ':7', ':8')
    dimensions = (17.0, 62.0, 63.0)  # rozmery [mm]

    def __init__(self, label):
        super().__init__(label)
        
            

class Quido88(Component):

    type = 'Quido 8/8'
    short = 'Binary IOs and temperature measurement'

    def __init__(self, label):
        super().__init__(label)        
    
class AD4ETH(Component):

    type = 'AD4ETH'
    short = 'AD converter with ethernet connection'

    def __init__(self, label):
        super().__init__(label)        
    
class DA2RS(Component):

    type = 'DA2RS'
    short = 'DA converter with RS485'

    def __init__(self, label):
        super().__init__(label)        
    
class GNOME(Component):

    type = 'GNOME'
    short = 'RS485 to ETHERNET'

    def __init__(self, label):
        super().__init__(label)        
    
class SENSYCON(Component):

    type = 'SENSYCON'
    short = 'PT100 to current converter'
    temp_range = (0, 100)       # rozsah teplot [degC]
    out_range = (4e-3, 20e-3)   # rozsah výstupních proudů [A]

    def __init__(self, label):
        super().__init__(label)        
    
class Rele(Component):

    type = 'Rele'
    short = 'Rele'

    def __init__(self, label):
        super().__init__(label)        
        

# Řídící počítač
PC(
    label = '-B10'
    ip = '192.168.1.90'
)
    
# Ethernet hub
Component(
    label = '-B11'
)
    
# Čidlo pro měření teploty vody na výstupu z kotle
PT100(
    label = '=KK-BTH' 
)    

# Čidlo pro měření teploty horké vody v přízemí
PT100(
    label = '=HP-BTH' 
)    


# Převodník na proudovou smyčku pro PT100 =HP-BTH
P5310(
    label = '-B3' 
    terminals = ()
)    
    
# Senzor teploty v obývacím pokoji v podkroví
TQS3(
     label =  '+204-BT'
     spinel_address = 50,
)
    
# Senzor venkovní teploty
TQS3(
    label = '+0-BT'
    spinel_address = 51
)
        
# Binární IO, 
Quido88(
    label = '-B1'
    spinel_address = 52
)
    
# Binární IO,
Quido88(
    label = '-B2'
    spinel_address = 53
),
    
# AD převodník, vstup 0: teplota kotle, vstup 1: horká větev v přízemí
AD4ETH(
    label = '-B3'
    spinel_address = 254  
    ip = '192.168.1.110'  
)
    
# DA převodník pro směšovací ventil
DA2RS(
    label = '-B4'
    spinel_address = 54
)
    
GNOME485(
    label = '-B5'
    ip = '192.168.1.111'
)
    
SENSYCON(
    label = '-B6'
)
    
P5310(
    label = '-B7'
)
    
Rele('-K1')
Rele('-K2')
Rele('-K3')
Rele('-K4')
Rele('-K5')
    
# Třífázový jistič
Component('-FA1') 
    
# Jednofázový jistič
Component('-FA2')
    
# Skříňka napájení
Component('-A1')
   
# Rozváděč řízení
Component('-A2')
    
# Napájecí zdroj
Component('-U1')
    
# Napájecí zdroj
Component('-U2')

Wire('=KK-BTH:1', '-B6:')
Wire('=KK-BTH:2', '-B6:')



)

signals = {

    # Třífázové napájecí napětí vstupní do jističe FA1
    ';U400'
    
    # Třífázové napájecí napětí za jističem FA1
    '-FA1;U'
    
    # Jednofázové napájecí napětí za jističek FA2
    '-FA2;U' : ('-FA2:2', '-U1:L', '-U2:L')
    
    # Prostě nulák
    ';N' : ('-U1:N', '-U2:N')
    

}


for c in components:
    print('{} & {}\\'.format(c, components[c])
