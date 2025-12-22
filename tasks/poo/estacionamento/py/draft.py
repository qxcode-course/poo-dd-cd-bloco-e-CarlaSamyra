from abc import ABC, abstractmethod

class Veiculo (ABC):
    def __init__ (self, id: str, tipo: str, hora_entrada: int):
        self.id = id
        self.tipo = tipo
        self.hora_entrada = hora_entrada
    
    @abstractmethod
    def calcular_Valor (self):
        pass

    def __str__ (self):
        tipo = self.tipo.rjust(10, "_")
        id = self.id.rjust(10, "_")
        return f"{tipo} : {id} : {self.hora_entrada}"
    
    def setEntrada(self, horaEntrada: int):
        self.hora_entrada = horaEntrada
        return horaEntrada
    
    def get_id (self):
        return self.id
    
    def get_tipo (self):
        return self.tipo

class Estacionamento: 
    def __init__ (self, hora_atual: int):
        self.hora_atual = hora_atual
        self.veiculos: list[Veiculo] = []

    def __str__(self):
        string = ""
        for i in self.veiculos:
            string += str(i) + "\n"
        string += f"Hora atual: {self.hora_atual}"
        return string
    
    def procurarVeiculo (self, id: str):
        for i, veiculo in enumerate(self.veiculos):
            if veiculo.get_id() == id:
                return i 
        return -1
    
    def pagar(self, id: str):
        index= self.procurarVeiculo(id)
        v = self.veiculos[index]
        valor = v.calcular_Valor(self.hora_atual)
        print(f"{v.tipo} chegou {v.hora_entrada} saiu {self.hora_atual}. Pagar R$ {valor:.2f}")
    
    def estacionar (self, tipo: str, id: str):
        if tipo == "bike":
            v = Bike(id, self.hora_atual)
        elif tipo == "moto":
            v = Moto(id, self.hora_atual)
        elif tipo == "carro":
            v = Carro(id, self.hora_atual)
        self.veiculos.append(v)

    def passarTempo (self, tempo: int):
        self.hora_atual += tempo

class Bike (Veiculo):
    def __init__(self, id: str, entrada: int):
        super().__init__(id, "Bike", entrada)
    
    def calcular_Valor(self, horaSaida: int):
        return 3

class Moto (Veiculo):
    def __init__ (self, id: str, entrada: int):
        super().__init__(id, "Moto", entrada)
    
    def calcular_Valor(self, horaSaida: int):
        tempo = horaSaida - self.hora_entrada
        return tempo / 20

class Carro (Veiculo):
    def __init__ (self, id: str, entrada: int):
        super().__init__(id, "Carro", entrada)

    def calcular_Valor(self, horaSaida: int):
        tempo = horaSaida - self.hora_entrada
        valor = tempo / 10
        return max(valor, 5.0)

def main():
    estacionamento = Estacionamento(0)
    while True:
        line = input()
        args: list[str] = line.split(" ")
        print ("$" + line)
        try:
            if args[0] == "end":
                break
            elif args[0] == "show":
                print(estacionamento)
            elif args[0] == "tempo":
                tempo = int(args[1])
                estacionamento.passarTempo(tempo)
            elif args[0] == "estacionar":
                tipo = args[1]
                id = args[2]
                estacionamento.estacionar(tipo, id)
            elif args[0] == "pagar":
                id = args[1]
                estacionamento.pagar(id)
            else:
                print("fail: comando inválido")
        except Exception as e:
            print(e)
main()

