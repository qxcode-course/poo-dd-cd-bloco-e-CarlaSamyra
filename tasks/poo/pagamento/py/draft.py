from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__ (self, valor: float, descricao: str):
        self.valor: float = valor 
        self.descricao: str = descricao
    
    def resumo (self):
        return f"Pagamento de R$ {self.valor}: {self.descricao}"
    
    def validar_valor (self):
        if self.valor <= 0:
            raise ValueError("Valor inválido")
        
    @abstractmethod
    def processar (self):
        pass

class CartaoCredito (Pagamento):
    def __init__ (self, numero: int, titular: str, limite: float, valor: float, descricao: str):
        super().__init__(valor, descricao)
        self.numero = numero
        self.titular = titular
        self.limite: float = limite
    
    def resumo (self):
        return f"Cartão de Crédito: " + super().resumo()
    
    def get_limite (self):
        return self.limite
    
    def processar (self):
        if self.valor > self.limite:
            print ("Erro, pagamento recusado. Limite insuficiente")
        self.limite -= self.valor

class Pix (Pagamento):
    def __init__ (self, chave: int, banco: str, descricao: str, valor: float):
        super().__init__(valor, descricao)
        self.chave = chave 
        self.banco = banco
    
    def processar (self):
        if self.valor < 0:
            print("Erro, valor de pagamento inválido")
        else:
            print(f"Pagamento realizado. Chave: {self.chave}, banco: {self.banco}")

class Boleto (Pagamento):
    def __init__ (self, codigo: float, vencimento: str, descricao: str, valor: float):
        super().__init__(valor, descricao)
        self.codigo = codigo
        self.vencimento = vencimento
    
    def processar (self):
        print ("Boleto gerado, aguarde o processamento...")
    
def processar_pagamentos (pagamentos: list [Pagamento]):
    for pag in pagamentos:
        pag.validar_valor()
        print(pag.resumo())
        pag.processar()
        if isinstance (pag, CartaoCredito):
            print (pag.get_limite())

pag: Pagamento = CartaoCredito(titular = "Carla", descricao = "Salgadinho", limite = 10.00, numero = 145, valor = 5.00)
pag1: Pagamento = Pix (chave = 123, banco = "inter", descricao = "esportiva", valor = 10.00)
pag2: Pagamento = Boleto (codigo = 4888.57, vencimento = "17/05", descricao = "camisa", valor = 10.00)
pagamentos: list [Pagamento] = [pag, pag1, pag2]
processar_pagamentos(pagamentos)