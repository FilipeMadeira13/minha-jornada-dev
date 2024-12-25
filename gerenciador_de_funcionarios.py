class GerenciadorDeFuncionarios:
    def __init__(self):
        """Inicializa o gerenciador com uma lista vazia de funcionarios."""
        self.funcionarios = []
        
    def adicionar_funcionario(self, funcionario):
        """Adiciona um funcionario à lista, verificando se o nome já existe."""
        if any(f.nome == funcionario.nome for f in self.funcionarios):
            print(f'Erro: Já existe um funcionário com o nome "{funcionario.nome}".')
        else:
            self.funcionarios.append(funcionario)
            print(f'Funcionário {funcionario.nome} adicionado com sucesso!')
            
    def exibir_funcionario(self, nome):
        """Exibe as informações de um funcionário pelo nome."""
        for funcionario in self.funcionarios:
            if funcionario.nome == nome:
                print(funcionario)
                return
        print(f'Funcionário com o nome "{nome}" não encontrado.')
        
    def aumentar_salario_funcionario(self, nome, porcentagem):
        """Aumenta o salário de um funcionário específico pela porcentagem dada."""
        for funcionario in self.funcionarios:
            if funcionario.nome == nome:
                funcionario.aumentar_salario(porcentagem)
                print(f'Salário de {funcionario.nome} atualizado com sucesso!')
                return
        print(f'Funcionário com o nome "{nome}" não encontrado.')
        
    def listar_funcionarios(self):
        """Lista todos os funcionários ordenados por cargo em ordem alfabética."""
        if not self.funcionarios:
            print('Nenhum funcionário cadastrado.')
            return
        
        funcionarios_ordenados = sorted(self.funcionarios, key=lambda f: f.cargo)
        print('\nLista de Funcionarios (ordenada por cargo):')
        for funcionario in funcionarios_ordenados:
            print(f'{funcionario}\n')