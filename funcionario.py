class Funcionario:
    def __init__(self, nome: str, idade: int, cargo: str, salario: float):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.salario = salario
        
    def __str__(self):
        """Exibe as informações de um funcionário específico."""
        return (f'Nome: {self.nome}\n'
                f'Idade: {self.idade}\n'
                f'Cargo: {self.cargo}\n'
                f'Salário: R$ {self.salario:.2f}\n')
        
    def aumentar_salario(self, porcentagem: float):
        """Aumenta o salário de um funcionário em uma porcentagem específica."""
        self.salario += self.salario * porcentagem / 100
        
        
        
