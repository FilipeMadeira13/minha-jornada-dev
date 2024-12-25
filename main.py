from funcionario import Funcionario
from gerenciador_de_funcionarios import GerenciadorDeFuncionarios

def main():
    """Testando o uso do programa."""
    gerenciador = GerenciadorDeFuncionarios()
    
    # Adicionando funcionários
    funcionario1 = Funcionario('João', 30, 'Desenvolvedor', 5000)
    funcionario2 = Funcionario('Ana', 28, 'Designer', 4000)
    gerenciador.adicionar_funcionario(funcionario1)
    gerenciador.adicionar_funcionario(funcionario2)
    
    # Exibindo um funcionário específico
    gerenciador.exibir_funcionario('João')
    
    # Aumentando o salário de um funcionario
    gerenciador.aumentar_salario_funcionario('João', 10)
    
    # Listando todos os funcionários
    gerenciador.listar_funcionarios()
    
if __name__ == '__main__':
    main()