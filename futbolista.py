from persona import Persona
from deportista import Deportista

class Futbolista (Persona, Deportista):
    
    listaFutbolistas = []
    
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        persona.__init__(self, nombre, edad, altura, sexo)
        deportista.__init__(self, "Futbol", añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)
        
    
    def getGolesMarcados(self):
        return self._golesMarcados
    
    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados
        
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas
        
    def getPiernaHabil(self):
        return self._piernaHabil
    
    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil
        
    
    def __str__(self):
        return f"Mi nombre es {persona.getNombre()} soy profesional en el deporte {deportista.getDeporte()} Tengo {persona.getEdaD()} años de edad y llevo {deportista.getAñosParticipando()} años en el deporte"       
    