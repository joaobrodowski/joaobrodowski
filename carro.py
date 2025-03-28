class veiculo:
    def __init__(self, marca, modelo,ano, placa):
        self. placa=placa 
        self. marca=marca
        self. modelo=modelo
        self. ano=ano
        self. __velocidade__=0#atribute privado
    def acelerar (self, incremento):
        self. __velocidade__ += incremento  
        print (f"{self.modelo}" acelerar para "{self.__velocidade__}")
    def mover (self):
        #método genérico que será sobrescrito
        pass



    class carro(veiculo):
        def mover(self):
            print("O carro {self.modelo}")




