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
    def __init__ (self, valor: float, descricao: str, numero: str, titular: str, limite: float):
        super().__init__(valor, descricao)
        self.numero = numero
        self.titular = titular
        self.limite: float = limite
    
    def processar (self):
        if self.valor > self.limite:
            print (f"Erro: Limite insuficiente no cartão {self.numero}")
        else:
            self.limite -= self.valor
            print (f"Pagamento aprovado no cartão. \n[Titular: {self.titular}. Limite restante: {self.limite}]")

class Pix (Pagamento):
    def __init__ (self, valor: float, descricao: str, chave: str, banco: str):
        super().__init__(valor, descricao)
        self.chave = chave 
        self.banco = banco
    
    def processar (self):
            print(f"PIX enviado via {self.banco} usando a chave {self.chave}")

class Boleto (Pagamento):
    def __init__ (self, valor: float, descricao: str, codigo: str, vencimento: str):
        super().__init__(valor, descricao)
        self.codigo = codigo
        self.vencimento = vencimento
    
    def processar (self):
        print ("Boleto gerado. Aguardando pagamento...")
    
def processar_pagamentos(pagamentos: list[Pagamento]):
    for pag in pagamentos:
        pag.validar_valor()
        tipo = type(pag).__name__.capitalize()
        print (pag.resumo())
        print ("Detalhes do pagamento:")
        print(f"Tipo: {tipo}")
        print(f"Valor: R$ {pag.valor:.2f}")
        print(f"Descrição: {pag.descricao}") 
        pag.processar()
        print("-" * 50)
        print()

pagamentos: list [Pagamento] = [Pix (valor = 200, descricao = "Tênis de corrida", chave = "pessoa@email.com", banco = "Banco Inter"), 
                                CartaoCredito(valor = 400, descricao = "Ingresso para show", numero = "3333 2222 1111 0000", titular = "Maria Silva", limite = 500),
                                Boleto (valor = 1000, descricao = "Pacote de viagem", codigo = "123456789", vencimento = "17-05-2026"),
                                CartaoCredito(valor = 900, descricao = "Tablet", numero = "4444 5555 6666 0000", titular = "Davi Silva", limite = 700)]
processar_pagamentos(pagamentos)