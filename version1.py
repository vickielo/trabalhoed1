class AtendimentoClientes:
    def __init__(self, num_caixas):
        self.num_caixas = num_caixas
        self.clientes_preferenciais = []
        self.clientes_comuns = []
        self.caixas_atendimento = [None] * num_caixas

    def retirar_senha(self, tipo_cliente):
        if tipo_cliente.lower() == 'preferencial':
            senha = 'P' + str(len(self.clientes_preferenciais) + 1)
            self.clientes_preferenciais.append(senha)
        elif tipo_cliente.lower() == 'comum':
            senha = 'C' + str(len(self.clientes_comuns) + 1)
            self.clientes_comuns.append(senha)
        else:
            print("Tipo de cliente inválido. Use 'preferencial' ou 'comum'.")
            return

        print(f"Senha gerada: {senha}")

    def chamar_cliente(self, num_caixa):
        if self.clientes_preferenciais:
            senha = self.clientes_preferenciais.pop(0)
        elif self.clientes_comuns:
            senha = self.clientes_comuns.pop(0)
        else:
            print("Não existem clientes esperando atendimento.")
            return

        self.caixas_atendimento[num_caixa - 1] = senha
        print(f"Chamando cliente {senha} para o caixa {num_caixa}")

    def consultar_clientes_em_espera(self):
        print("Clientes preferenciais em espera:", self.clientes_preferenciais)
        print("Clientes comuns em espera:", self.clientes_comuns)

    def consultar_estado_caixas(self):
        for i, senha in enumerate(self.caixas_atendimento, start=1):
            print(f"Caixa {i}: {senha if senha else 'Livre'}")

def main():
    num_caixas = int(input("Informe a quantidade de caixas (entre 2 e 20): "))
    if num_caixas < 2 or num_caixas > 20:
        print("Quantidade de caixas inválida. Encerrando o programa.")
        return

    atendimento = AtendimentoClientes(num_caixas)

    while True:
        print("\nMenu:")
        print("1. Retirada de senha")
        print("2. Chamar cliente")
        print("3. Consultar clientes em espera")
        print("4. Consultar estado dos caixas")
        print("5. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            tipo_cliente = input("Informe o tipo de cliente (preferencial ou comum): ")
            atendimento.retirar_senha(tipo_cliente)
        elif opcao == 2:
            num_caixa = int(input("Informe o número do caixa: "))
            atendimento.chamar_cliente(num_caixa)
        elif opcao == 3:
            atendimento.consultar_clientes_em_espera()
        elif opcao == 4:
            atendimento.consultar_estado_caixas()
        elif opcao == 5:
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
